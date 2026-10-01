# Markdown bemutatása
A bemutatás a [Github dokumentációja](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) alapján készült.

FONTOS! Ez a markdown leírás a Github Markdown feldolgozójához készült, így előfordulhat, hogy más markdown feldolgozó egyes formázási lehetőséget NEM FOGAD EL! (Pl. HTML tagek)

Összeállította: [Banic Tibor](https://github.com/BanicTibor/)

# Bekezdések
Új bekezdéshez két sor között hagyjunk egy üres sort.

# Sortörés
Sortöréshez a sor végén hagyjunk 2 space-t, majd új sorban folytassuk a paragrafust. Másik lehetőség a `<br>` HTML-tag használata.
# Fejlécek
Fejlécet A # karakterrel lehet tenni. A # után szóközt kell tenni! Ahány # annyiadik szintű fejléc. (Maximum H6-os szintű fejléc létezik!)
Példák:
# H1
## H2
###### H6

# Félkövér
Egy szöveg **félkövérré** tételéhez `** **` VAGY `__ __` közé kell tenni.  
Ezek mellett lehetőség van a webes szerkesztőben lehetőség van gyorsbillentyűvel is kitenni:  
`Ctrl`+`B` VAGY `Command`+`B`

# Dőlt
Egy szöveg *dőlté* tételéhez `* *` VAGY `_ _` közé kell tenni.  
Ezek mellett lehetőség van a webes szerkesztőben lehetőség van gyorsbillentyűvel is kitenni:  
`Ctrl`+`I` VAGY `Command`+`I`

# Félkövér és dölt vegyítése
Ahhoz, hogy egy szövegben vegyesen lehessen használni, ahhoz ellentétesen kell használni * és _ karaktert.  
Azaz ha egy szövegben már csillagal félkövérré tettem a szöveget már benne nem tehetem még dőlté csillaggal, helyette alsó kötőjelet kell használni.

Példa:  
`**Ez félkövér, _de ez már félkövér és dőlt._ Itt viszont ismét csak félkövér.**`  
**Ez félkövér, _de ez már félkövér és dőlt._ Itt viszont ismét csak félkövér.**

# Félkövér és dőlt
***Kombinált félkövér és dőlt*** formázásra is lehetőség van, ehhez `*** ***` közé kell tenni a szöveget.

# Áthúzás
Egy szöveg ~~áthúzottá~~ tételéhez `~~ ~~` VAGY `~ ~` közé kell tenni.

# Alsó index
Alsó index HTML-tag -el oldható meg: `<sub> </sub>`  
S<sub>n</sub>

# Felső index
Felső index HTML-tag -el oldható meg: `<sup> </sup>`  
2<sup>10</sup>

# Aláhúzás
<ins>Aláhúzás</ins> HTML-tag -el oldható meg: `<ins> </ins>`

# Idézés
Idézéshez a sor elejére a > karaktert kell kitenni.
> Az önműködő biztosított térközjelző árbóca fehér színű.
A fehér árbóc azt jelzi, hogy a vonat olyan főjelzőhöz érkezett,
amely mellett Megállj! jelzés esetén vagy ha a jelző sötét, az
F.2. sz. Forgalmi Utasítás előírásai szerint el szabad haladni

-- [F.1. számú Forgalmi Utasítás](https://www.mavcsoport.hu/sites/default/files/upload/page/f.1._sz._jelzesi_utasitas_1-_4._mod._egyseges_szerkezetben_2023.04.01-tol_hatalyos.pdf)

# Kód
Kód idézéshez kettő ` közé kell tenni a kódot.

# Több soros kód részlet
Több soros kódhoz a részlet előtti sorba és utáni sorba ` ``` ` kell tenni.

# Szín jelölés
Szín jelölése lehetséges, ha kód részletbe színkódot (HEX, RGB, HSL) teszünk.
`#RRGGBB`

# Linkelés
[Link](https://github.com/BanicTibor)hez először a linkelendő szöveget helyezzük `[]` közé, majd közvetlenül utána `()` közé a linket.

# Kép
Kép beillesztéséhez `!` után `[]` közé írjunk hellyettesítő szöveget a kép sikertelen betöltése eseténre, majd `()` közé a kép elérhetőségét.

# Listák

## Rendezett
Rendezett felsoroláshoz sorszámozzuk a sorokat a sor elején.
1. Első elem
2. Második elem
3. Harmadik elem

## Rendezetlen
Rendezetlen felsoroláshoz a sorokat kötőjellel jelöljük.
- Első elem
- Második elem
- Harmadik elem

# Feladat lista
Feladat lista kezdéséhez rendezetlen lista elemeinek kezdeténél `[ ]` használunk üres jelölő négyzethez vagy `[x]` -et kitöltött jelölő mégyzethez.
- [ ] Nincs kész
- [x] Kész

# Emojik :melting_face:
Emojik is beilleszthetők, ehhez cheatsheetért [KATT IDE!](https://github.com/ikatyang/emoji-cheat-sheet/blob/github-actions-auto-update/README.md)

# Figyelmeztetések
Figyelmeztetések tehetők idézés felhasználásával. Több is létezik: [!NOTE] [!TIP] [!IMPORTANT] [!WARNING] [!CAUTION]
Példa:
```
> [!NOTE]
> Megjegyzés
```
> [!NOTE]
> Megjegyzés

# Formázás megszakítás
Ha szeretnénk, hogy a markdown alkalmazás egy adott formázó karaktert, ne értelmezzen formázásként, tegyünk elé egy \ jelet.  
Példa:  
`\*\*Ez nem szeretném, hogy dőlt legyen\*\*`  
\*\*Ez nem szeretném, hogy dőlt legyen\*\*

# Táblázat
Táblázat egyszerűen készíthető karakterekkel való rajzolással.
Példa:
```
| Első oszlop | Második oszlop |
| --- | --- |
| Cella | Cella |
| Cella | Cella |
```
| Első oszlop | Második oszlop |
| ----------- | --- |
| Cella | Cella |
| Cella | Cella |

## Igazítás is lehetséges
Példa:
```
| Balra igazított | Középre igazított | Jobbra igazított |
| :--- | :---: | ---: |
| Cella | Cella | Cella |
| Cella | Cella | Cella |
```
| Balra igazított | Középre igazított | Jobbra igazított |
| :--- | :---: | ---: |
| Cella | Cella | Cella |
| Cella | Cella | Cella |

# Összecsukható szekció
Összecsukható szekciót `<details> </details>` tag-ek határolják körbe. Címet a `<summary> </summary>` tag-ekkel lehetséges megadni.  
Példa:
```
<details>
<summary>Szekció</summary>

Sekció tartalma
</details>
```
<details>
<summary>Szekció</summary>

Sekció tartalma
</details>

# Vízszintes elválasztó vonal
Vízszintes elválasztó vonal elhelyezéséhez egy sorban legalább 3 kötőjelet kell elhelyezni.