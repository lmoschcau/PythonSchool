unit dynalist;
(*-----------------------------------------------------------------------*)
(* Allgemeiner Datentyp LISTE.INC, einfach verkettete lineare Liste      *)
(* Implementation mit dem Datentyp Pointer                               *)
(*-----------------------------------------------------------------------*)
(* Der Benutzer muss den "Listeninfotyp" importieren und dafueÅr Ein- und  *)
(* Ausgabeprozeduren zur VerfÅgung stellen. Es steht dann der Datentyp   *)
(* "Listentyp" zur VerfÅgung.                                            *)
(*-----------------------------------------------------------------------*)

INTERFACE

uses crt,importdy;

TYPE  Dateinametyp     = STRING [30];
      Listenzeigertyp  = ^Listenknotentyp;
      Listenknotentyp  = RECORD
                         Inhalt:           Listeninfotyp;
                         Nachfolgerzeiger: Listenzeigertyp;
                         END;
      Listentyp        = RECORD
                         Kopfzeiger, Aktuellzeiger: Listenzeigertyp;
                         END;          (* zeigt VOR das aktuelle Element *)


(*====================== Deklaration der Prozeduren =========================*)

PROCEDURE Erzeuge_leere_Liste (VAR Liste: Listentyp);
(* Pre:  beliebig                                                            *)
(* Post: Es wird eine leere Liste erzeugt. Ferner wird eine Freiliste ange-  *)
(*       legt.                                                               *)

FUNCTION Liste_leer (Liste: Listentyp): BOOLEAN;
(* Pre:  Die Liste existiert.                                                *)
(* Post: Falls die Liste leer ist, wird der Funktionswert True, andernfalls  *)
(*       False zurÅckgegeben.                                                *)

FUNCTION Liste_zuende (Liste: Listentyp): BOOLEAN;
(* Pre:  Die Liste existiert.                                                *)
(* Post: Falls das letzte Listenelement erreicht ist, wird der Funktionswert *)
(*       True, andernfalls False zurÅckgegeben.                              *)

PROCEDURE Beginne_am_Listenanfang (VAR Liste: Listentyp);
(* Pre:  Die Liste existiert.                                                *)
(* Post: Der Listenzeiger wird auf den Listenanfang (Dummy) gesetzt.         *)

PROCEDURE Ruecke_in_der_Liste_vor (VAR Liste: Listentyp);
(* Pre:  Die Liste existiert.                                                *)
(* Post: Die Prozedur rÅckt den Listenzeiger um 1 Stelle weiter, falls das   *)
(*       Listenende noch nicht erreicht ist.                                 *)

PROCEDURE Lies_Listenelement (Liste: Listentyp;
                              VAR Inhalt: Listeninfotyp);
(* Pre:  Die Liste existiert.                                                *)
(* Post: Die Prozedur liefert den Inhalt des betrachteten Listenelementes.   *)

PROCEDURE Fuege_Listenelement_ein (Liste: Listentyp;
                                   Inhalt: Listeninfotyp);
(* Pre:  Die Liste existiert.                                                *)
(* Post: FÅgt den Åbergebenen Inhalt als neues Element VOR das Element ein,  *)
 (*      auf das der Listenzeiger weist. Danach zeigt der Listenzeiger auf   *)
 (*      das neu eingefÅgte Element.                                         *)

PROCEDURE Loesche_Listenelement (Liste: Listentyp);
(* Pre:  Die Liste existiert.                                                *)
(* Post: Lîscht das aktuelle Listenelement, der Zeiger bleibt dabei stehen,  *)
(*       d.h. er weist danach auf das folgende, nachgerutschte Element.      *)

FUNCTION Listenknotenzahl (Liste: Listentyp): INTEGER;
(* Pre:  Die Liste existiert.                                                *)
(* Post: Die Funktion ermittelt die Anzahl der Listenelemente. Die Liste     *)
(*       bleibt unverÑndert.                                                 *)

PROCEDURE Entferne_Liste (VAR Liste: Listentyp);
(* Pre:  Die Liste existiert.                                                *)
(* Post: Gibt den Speicher wieder frei, indem alle Listenelemente au·er dem  *)
(*       Dummy gelîscht werden. Es entsteht eine leere Liste.                *)

PROCEDURE Sichere_Liste (Liste: Listentyp;
                         Dateiname: Dateinametyp);
(* Pre:  Die Liste existiert.                                                *)
(* Post: Sichert die verkettete Liste unter dem gewÅnschten Dateinamen auf   *)
(*       der Diskette als sequentielle Datei.                                *)

PROCEDURE Lade_Liste (VAR Liste: Listentyp;
                      Dateiname: Dateinametyp);
(* Pre:  Die Liste existiert.                                                *)
(* Post: LÑdt eine sequentielle Datei gleicher Elementstruktur und reorgani- *)
(*       siert die Verkettung.                                               *)



(*========== Es folgt die Implementation (nur etwas fÅr Insider!) ===========*)

IMPLEMENTATION

function frageja(satz:string):boolean;
var taste : char;
begin
 write(satz,' <j/n> ?');
 repeat
  taste:=readkey;
 until taste in ['J','j','N','n'];
 writeln;
 frageja:=taste in ['J','j'];
end;


PROCEDURE Erzeuge_leere_Liste;
BEGIN
(* Leere Liste mit dem Dummy einrichten *)
WITH Liste DO
     BEGIN
     New(Kopfzeiger);
     Kopfzeiger^.Nachfolgerzeiger := NIL;
     Aktuellzeiger := Kopfzeiger;
     END;
END;
(*---------------------------------------------------------------------------*)
FUNCTION Liste_leer;
BEGIN
WITH Liste DO
     Liste_leer := (Kopfzeiger^.Nachfolgerzeiger = NIL);
END;
(*---------------------------------------------------------------------------*)
FUNCTION Liste_zuende;
BEGIN
WITH Liste DO
     Liste_zuende := (Aktuellzeiger^.Nachfolgerzeiger = NIL);
END;
(*---------------------------------------------------------------------------*)
PROCEDURE Beginne_am_Listenanfang;
BEGIN
WITH Liste DO
     Aktuellzeiger := Kopfzeiger;
END;
(*---------------------------------------------------------------------------*)
PROCEDURE Ruecke_in_der_Liste_vor;
BEGIN
IF   NOT LISTE_ZUENDE (Liste)
THEN WITH Liste DO
          Aktuellzeiger := Aktuellzeiger^.Nachfolgerzeiger;
END;
(*---------------------------------------------------------------------------*)
PROCEDURE Lies_Listenelement;
VAR Hilfszeiger: listenzeigertyp;
BEGIN
WITH Liste DO
     IF   NOT LISTE_ZUENDE (Liste)
     THEN BEGIN
          Hilfszeiger := Aktuellzeiger^.Nachfolgerzeiger;
          Inhalt := Hilfszeiger^.Inhalt;
          END;
END;
(*---------------------------------------------------------------------------*)
PROCEDURE Fuege_Listenelement_ein;
VAR Neuzeiger: Listenzeigertyp;
BEGIN
     (* freien Platz schaffen und dort den Listenknoten speichern *)
     New(Neuzeiger);
     Neuzeiger^.Inhalt := Inhalt;
     (* das neue Element in die Liste einfÅgen *)
     WITH Liste DO
          BEGIN
          (* an das neue Element die Restliste anfÅgen *)
          (* -> Wert zuweisen *)
          Neuzeiger^.Nachfolgerzeiger := Aktuellzeiger^.Nachfolgerzeiger;
          (* das neue Element mit Restliste an den VorgÑnger hÑngen *)
          (* -> Speicherverweis zuweisen / "linken" *)
          Aktuellzeiger^.Nachfolgerzeiger := Neuzeiger;
          END;
END;
(*---------------------------------------------------------------------------*)
PROCEDURE Loesche_Listenelement;
VAR Loeschzeiger: Listenzeigertyp;
BEGIN
IF   NOT LISTE_ZUENDE (Liste)
THEN BEGIN
     (* das zu lîschende Element aus der Liste entfernen *)
     WITH Liste DO
          BEGIN
          Loeschzeiger := Aktuellzeiger^.Nachfolgerzeiger;
          (* Beim VorgÑnger des Lîschelements den Verweis auf den
             Nachfolger des Lîschelements notieren *)
          Aktuellzeiger^.Nachfolgerzeiger :=
          Loeschzeiger^.Nachfolgerzeiger;
          END;
     dispose(Loeschzeiger);
     END;
END;
(*---------------------------------------------------------------------------*)
FUNCTION Listenknotenzahl;
VAR Zaehler: INTEGER;
    Element: Listeninfotyp;
BEGIN
BEGINNE_AM_LISTENANFANG (Liste);
Zaehler := 0;
WHILE NOT LISTE_ZUENDE (Liste) DO
      BEGIN
      LIES_LISTENELEMENT (Liste, Element);
      Zaehler := Zaehler + 1;
      RUECKE_IN_DER_LISTE_VOR (Liste);
      END;
Listenknotenzahl := Zaehler;
END;
(*---------------------------------------------------------------------------*)
PROCEDURE Entferne_Liste;                                (* 8.2.3 Aufgabe 2 *)
BEGIN
 beginne_am_listenanfang(Liste);
 while not Liste_zuende(liste) do
  begin
   loesche_listenelement(Liste);
  end;
END;
(*---------------------------------------------------------------------------*)
PROCEDURE Sichere_Liste;
                               (* 8.2.3 Aufgabe 3 *)
var datei   : file of Listeninfotyp;
    Element : Listeninfotyp;
BEGIN
    assign(datei,dateiname);
    rewrite(datei);
    BEGINNE_AM_LISTENANFANG (Liste);
     WHILE NOT LISTE_ZUENDE (Liste) DO
      BEGIN
      LIES_LISTENELEMENT (Liste, Element);
      write(datei,Element);
      RUECKE_IN_DER_LISTE_VOR (Liste);
      END;
    close(Datei);

END;
(*---------------------------------------------------------------------------*)
PROCEDURE Lade_Liste;                                    (* 8.2.3 Aufgabe 4 *)
var datei   : file of Listeninfotyp;
    Zaehler:integer;
    Element : Listeninfotyp;
BEGIN
    entferne_liste(liste);
    assign(datei, Dateiname);
    reset(datei);
    for Zaehler:=filesize(datei)-1 downto 0 do
     begin
      seek(datei,Zaehler);
      read(datei,element);
      Fuege_Listenelement_ein (Liste,Element);
     end;
    close(datei);
END;
(*============================= Das war's ! =================================*)
begin
end.