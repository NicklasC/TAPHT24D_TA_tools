
1a. "Fiskarna som jag fångade var 55 cm långa."
Svar: [\d]+ cm

1b. Denna gången vill vi veta om det finns två längder.
Exempel: 
    "Fiskarna som jag fångade var 55 cm långa. Räven jag fångade var 65 cm lång"
(\d+\s*cm).*?(\d+\s*cm)


2. Skriv ett regex som matchar ett svenskt postnummer. Postnummer består av fem siffror indelade i två grupper med mellanslag emellan.
Exempel: "123 45"
Svar: (\d{3}\s?\d{2})

3. Skriv ett regex som matchar ett datum skrivet enligt den internationella standarden ISO 8601, alltså 10 tecken med bindestreck mellan avdelningarna. 
Exempel: 2025-03-10
Svar: (\d{4}-\d{2}-\d{2})
Notera: Detta testar inte att man skrivit in max 12 månader eller antal dagar per månad.. och det tänker jag inte skriva ett uttryck för =).

4. Skriv ett regex som matchar ett pengavärde i siffror. 
Exempel på värden som ska matchas:
200 kr regexp: (\d+\skr)
12,50 kr (\d+,\d+ kr)
0,35 kr som ovan
Svar: (\d+\skr)|(\d+,\d+ kr)


