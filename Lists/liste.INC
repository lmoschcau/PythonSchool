{Man kann auch eine unit draus werkeln!}

(*-----------------------------------------------------------------------*)
(* Allgemeiner Datentyp LISTE.INC, einfach verkettete lineare Liste      *)
(* Implementation mit dem Datentyp ARRAY                                 *)
(* 
(*-----------------------------------------------------------------------*)
(* Der Benutzer muss den "Listeninfotyp" importieren und dafÅr Ein- und   *)
(* Ausgabeprozeduren zur VerfÅgung stellen. Es steht dann der Datentyp   *)
(*"Listentyp" zur VerfÅgung.                                             *)
(*-----------------------------------------------------------------------*)

CONST Speichergroesse  = 100;  (* beliebig verÑnderbar *)

TYPE  Dateinametyp     = STRING [30];
      Listenzeigertyp  = 0..Speichergroesse;
      Listenknotentyp  = RECORD
                         Inhalt:           Listeninfotyp;
                         Nachfolgerzeiger: Listenzeigertyp;
                         END;
      Listentyp        = RECORD
                         Kopfzeiger, Aktuellzeiger: Listenzeigertyp;
                         END;          (* zeigt VOR das aktuelle Element *)
      Speichertyp      = ARRAY [1..Speichergroesse] OF Listenknotentyp;

VAR Freiliste: Listentyp;
    Speicher: Speichertyp;

(*====================== Deklaration der Prozeduren =========================*)

PROCEDURE Erzeuge_leere_Liste (VAR Liste: Listentyp); FORWARD;
(* Pre:  beliebig                                                            *)
(* Post: Es wird eine leere Liste erzeugt. Ferner wird eine Freiliste ange-  *)
(*       legt.                                                               *)

FUNCTION Liste_leer (Liste: Listentyp): BOOLEAN;  FORWARD;
(* Pre:  Die Liste existiert.                                                *)
(* Post: Falls die Liste leer ist, wird der Funktionswert True, andernfalls  *)
(*       False zurÅckgegeben.                                                *)

FUNCTION Liste_zuende (Liste: Listentyp): BOOLEAN; FORWARD;
(* Pre:  Die Liste existiert.                                                *)
(* Post: Falls das letzte Listenelement erreicht ist, wird der Funktionswert *)
(*       True, andernfalls False zurÅckgegeben.                              *)

PROCEDURE Beginne_am_Listenanfang (VAR Liste: Listentyp); FORWARD;
(* Pre:  Die Liste existiert.                                                *)
(* Post: Der Listenzeiger wird auf den Listenanfang (Dummy) gesetzt.         *)

PROCEDURE Ruecke_in_der_Liste_vor (VAR Liste: Listentyp); FORWARD;
(* Pre:  Die Liste existiert.                                                *)
(* Post: Die Prozedur rÅckt den Listenzeiger um 1 Stelle weiter, falls das   *)
(*       Listenende noch nicht erreicht ist.                                 *)

PROCEDURE Lies_Listenelement (Liste: Listentyp;
                              VAR Inhalt: Listeninfotyp); FORWARD;
(* Pre:  Die Liste existiert.                                                *)
(* Post: Die Prozedur liefert den Inhalt des betrachteten Listenelementes.   *)

PROCEDURE Fuege_Listenelement_ein (Liste: Listentyp;
                                   Inhalt: Listeninfotyp); FORWARD;
(* Pre:  Die Liste existiert.                                                *)
(* Post: FÅgt den Åbergebenen Inhalt als neues Element VOR das Element ein,  *)
 (*      auf das der Listenzeiger weist. Danach zeigt der Listenzeiger auf   *)
 (*      das neu eingefÅgte Element.                                         *)

PROCEDURE Loesche_Listenelement (Liste: Listentyp); FORWARD;
(* Pre:  Die Liste existiert.                                                *)
(* Post: Lîscht das aktuelle Listenelement, der Zeiger bleibt dabei stehen,  *)
(*       d.h. er weist danach auf das folgende, nachgerutschte Element.      *)

FUNCTION Listenknotenzahl (Liste: Listentyp): INTEGER; FORWARD;
(* Pre:  Die Liste existiert.                                                *)
(* Post: Die Funktion ermittelt die Anzahl der Listenelemente. Die Liste     *)
(*       bleibt unverÑndert.                                                 *)

PROCEDURE Entferne_Liste (VAR Liste: Listentyp); FORWARD;
(* Pre:  Die Liste existiert.                                                *)
(* Post: Gibt den Speicher wieder frei, indem alle Listenelemente au·er dem  *)
(*       Dummy gelîscht werden. Es entsteht eine leere Liste.                *)

PROCEDURE Sichere_Liste (Liste: Listentyp;
                         Dateiname: Dateinametyp); FORWARD;
(* Pre:  Die Liste existiert.                                                *)
(* Post: Sichert die verkettete Liste unter dem gewÅnschten Dateinamen auf   *)
(*       der Diskette als sequentielle Datei.                                *)

PROCEDURE Lade_Liste (VAR Liste: Listentyp;
                      Dateiname: Dateinametyp); FORWARD;
(* Pre:  Die Liste existiert.                                                *)
(* Post: LÑdt eine sequentielle Datei gleicher Elementstruktur und reorgani- *)
(*       siert die Verkettung.                                               *)

(*========== Es folgt die Implementation (nur etwas fÅr Insider!) ===========*)

PROCEDURE Erzeuge_leere_Liste;
VAR Index: 1..Speichergroesse;
BEGIN
(* Leere Liste mit dem Dummy einrichten *)
WITH Liste DO
     BEGIN
     Kopfzeiger := 1;
     Aktuellzeiger := 1;
     Speicher [Kopfzeiger].Nachfolgerzeiger := 0;
     END;
(* Freiliste einrichten *)
WITH Freiliste DO
     BEGIN
     Kopfzeiger := 2;
     FOR Index := 2 TO Speichergroesse - 1 DO
         Speicher [Index].Nachfolgerzeiger := Index + 1;
     Speicher [Speichergroesse].Nachfolgerzeiger := 0;
     END;
END;
(*---------------------------------------------------------------------------*)
FUNCTION Liste_leer;
BEGIN
WITH Liste DO
     Liste_leer := (Speicher [Kopfzeiger].Nachfolgerzeiger = 0);
END;
(*---------------------------------------------------------------------------*)
FUNCTION Liste_zuende;
BEGIN
WITH Liste DO
     Liste_zuende := (Speicher [Aktuellzeiger].Nachfolgerzeiger = 0);
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
          Aktuellzeiger := Speicher [Aktuellzeiger].Nachfolgerzeiger;
END;
(*---------------------------------------------------------------------------*)
PROCEDURE Lies_Listenelement;
VAR Hilfszeiger: listenzeigertyp;
BEGIN
WITH Liste DO
     IF   NOT LISTE_ZUENDE (Liste)
     THEN BEGIN
          Hilfszeiger := Speicher [Aktuellzeiger].Nachfolgerzeiger;
          Inhalt := Speicher [Hilfszeiger].Inhalt;
          END;
END;
(*---------------------------------------------------------------------------*)
PROCEDURE Fuege_Listenelement_ein;
VAR Neuzeiger: Listenzeigertyp;
BEGIN
IF   NOT LISTE_LEER (Freiliste)
THEN BEGIN
     WITH Freiliste DO        (* der Freiliste einen freien Platz entnehmen *)
          BEGIN
          Neuzeiger := Kopfzeiger;
          Kopfzeiger := Speicher [Kopfzeiger].Nachfolgerzeiger;
          END;
     Speicher [Neuzeiger].Inhalt := Inhalt;   (* den neuen Inhalt eintragen *)
     WITH Liste DO
          BEGIN                               (* das neue Element einfÅgen  *)
          Speicher [Neuzeiger].Nachfolgerzeiger :=
          Speicher [Aktuellzeiger].Nachfolgerzeiger;
          (* das neue Element mit Restliste an den VorgÑnger hÑngen *)
          Speicher [Aktuellzeiger].Nachfolgerzeiger := Neuzeiger;
          END;
    END
ELSE BEGIN
     WRITELN ('Kein Speicherplatz mehr vorhanden! - Weiter mit RETURN');
     READLN;
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
          Loeschzeiger := Speicher [Aktuellzeiger].Nachfolgerzeiger;
          (* Beim VorgÑnger des Lîschelements den Verweis auf den
             Nachfolger des Lîschelements notieren *)
          Speicher [Aktuellzeiger].Nachfolgerzeiger :=
          Speicher [Loeschzeiger].Nachfolgerzeiger;
          END;
     (* das gelîschte Element in die Freiliste einfÅgen *)
     WITH Freiliste DO
          BEGIN
          (* die Freiliste an das Lîschelement anhÑngen *)
          Speicher [Loeschzeiger].Nachfolgerzeiger := Kopfzeiger;
          (* das Lîschelement mit der Freiliste im Freilistenkopf verankern *)
          Kopfzeiger := Loeschzeiger;
          END;
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
PROCEDURE Entferne_Liste;
BEGIN                                  (* 8.2.3 Aufgabe 2 *)

END;
(*---------------------------------------------------------------------------*)
PROCEDURE Sichere_Liste;
VAR Datei: FILE OF Listeninfotyp;      (* 8.2.3 Aufgabe 3 *)
    Inhalt: Listeninfotyp;
BEGIN

END;
(*---------------------------------------------------------------------------*)
PROCEDURE Lade_Liste;
VAR Datei: FILE OF Listeninfotyp;      (* 8.2.3 Aufgabe 4 *)
    Inhalt: Listeninfotyp;
BEGIN


END;
(*============================= Das war's ! =================================*)
