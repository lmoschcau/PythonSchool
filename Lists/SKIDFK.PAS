

PROGRAM SKIDFK;  (* 8.2.2 / Aufgabe 1 *)
uses crt,dynalist,importdy;
{TYPE Listeninfotyp = RECORD
                     Name: STRING [20];
                     Zeit: REAL;
                     END; }
 {(*$I LISTE.INC*) }

VAR Skiliste: Listentyp;
    Antwort: CHAR;

   PROCEDURE Suche_Einfuegestelle (VAR Liste: Listentyp; Neu: Listeninfotyp);
   VAR Vergleichsinhalt: Listeninfotyp;
       Abbruch: BOOLEAN;
   BEGIN
   BEGINNE_AM_LISTENANFANG (Liste);
   IF   NOT LISTE_LEER (Liste)
   THEN BEGIN
        LIES_LISTENELEMENT (Liste, Vergleichsinhalt);
        Abbruch := (Vergleichsinhalt.Zeit > Neu.Zeit) OR
                   LISTE_ZUENDE (Liste);
        WHILE NOT Abbruch DO
              BEGIN
              RUECKE_IN_DER_LISTE_VOR (Liste);
              IF   NOT LISTE_ZUENDE (Liste)
              THEN LIES_LISTENELEMENT (Liste, Vergleichsinhalt);
              Abbruch := (Vergleichsinhalt.Zeit > Neu.Zeit) OR
                          LISTE_ZUENDE (Liste);
              END;
        END;
   END;


   PROCEDURE Einen_Skifahrer_hinzufuegen;
   VAR Skifahrer: Listeninfotyp;
   BEGIN
   WITH Skifahrer DO
        BEGIN
        WRITE ('Name des Skifahrers: ');
        READLN (Name);
        WRITE ('Gelaufene Zeit: ');
        READLN (Zeit);
        END;
   SUCHE_EINFUEGESTELLE (Skiliste, Skifahrer);
   FUEGE_LISTENELEMENT_EIN (Skiliste, Skifahrer);
   END;


   PROCEDURE Einen_Skifahrer_streichen;
   VAR Skifahrer: Listeninfotyp;
       Gefunden: BOOLEAN;
       i,Stelle:integer;

     PROCEDURE Suche (VAR Liste: Listentyp; Inhalt: Listeninfotyp;
                      VAR Gefunden: BOOLEAN;var stelle:integer);
     VAR Vergleichsinhalt: Listeninfotyp;
         Abbruch: BOOLEAN;
     begin
         BEGINNE_AM_LISTENANFANG (Liste);
         stelle:=0;
        IF   NOT LISTE_LEER (Liste)
        THEN BEGIN
        LIES_LISTENELEMENT (Liste, Vergleichsinhalt);
        stelle:=stelle+1;
        Gefunden:=(Vergleichsinhalt.name=inhalt.name);
        Abbruch := (Vergleichsinhalt.name = Inhalt.name) OR
                    LISTE_ZUENDE (Liste);
        WHILE NOT Abbruch DO
              BEGIN
              RUECKE_IN_DER_LISTE_VOR (Liste);
              stelle:=stelle+1;
              IF   NOT LISTE_ZUENDE (Liste)
              THEN LIES_LISTENELEMENT (Liste, Vergleichsinhalt);
              Gefunden:=(Vergleichsinhalt.name=inhalt.name);
              Abbruch := (Vergleichsinhalt.name = Inhalt.name) OR
                          LISTE_ZUENDE (Liste);
              END;
        END;
     END;  (* Suche *)

   BEGIN  (* Einen_Skifahrer_streichen *)
    WITH Skifahrer DO
        BEGIN
        WRITE ('Name des Skifahrers: ');
        READLN (Name);
        WRITE ('Gelaufene Zeit: ');
        READLN (Zeit);
        END;
   SUCHE(Skiliste, Skifahrer,Gefunden,stelle);
   Beginne_am_Listenanfang(Skiliste);
   for i:=1 to stelle do
    ruecke_in_der_Liste_vor(Skiliste);

   END;


   PROCEDURE Ski_Bestenliste_ausgeben;
   VAR Skifahrer: Listeninfotyp;
   BEGIN
   WRITELN;
   BEGINNE_AM_LISTENANFANG (Skiliste);
   WHILE NOT LISTE_ZUENDE (Skiliste) DO
         BEGIN
         LIES_LISTENELEMENT (Skiliste, Skifahrer);
         WITH Skifahrer DO
              WRITELN (Name, Zeit:8:2);
         RUECKE_IN_DER_LISTE_VOR (Skiliste);
         END;
   WRITELN;
   WRITELN ('Weiter mit RETURN');
   READLN;
   END;


BEGIN  (* Ski_Bestenliste *)
ERZEUGE_LEERE_LISTE (Skiliste);
REPEAT REPEAT CLRSCR;
              WRITELN ('A : Einen Skifahrer hinzufÅgen');
              WRITELN ('B : Einen Skifahrer streichen');
              WRITELN ('C : Ski-Bestenliste ausgeben');
              WRITELN ('D : Ende');
              writeln ('E : Liste laden');
              writeln ('F : Liste speicher');
              WRITELN;
              WRITE ('Ihre Wahl: ');
              READLN (Antwort);
       UNTIL  Antwort IN ['A'..'F','a'..'f'];
       CASE Antwort OF
            'A','a' : EINEN_SKIFAHRER_HINZUFUEGEN;
            'B','b' : EINEN_SKIFAHRER_STREICHEN;
            'C','c' : SKI_BESTENLISTE_AUSGEBEN;
            'E','e' : lade_liste(Skiliste,'Ski.dat');
            'F','f' : sichere_liste(Skiliste,'Ski.dat');
       END;
UNTIL  Antwort IN ['D','d'];
END.
