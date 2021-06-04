# Zodiac Statistic Tool
**CZ**
## Prerekvizity
- Python 3
- Facebook nebo seznam Vašich přátel a jejich znamení zvěrokruhu
- hodně času

## Návod k přípravě dat
### Předmluva k formátu dat
Tento tool bere jako vstup textový soubor v kódování UTF-8 ve formátu dat CSV.

Formát sloupců je:
*znameni; vibe; kkt*

**Znamení** je ve formátu string a označuje jaké znamení je váš přítel
**Vibe** je numerická hodnota od 0 do 10, která označuje, jak moc s tím člověkem vajbíte
**Kkt** je numerická hodnota od 0 do 10, která označuje, jak moc je ten člověk kikot

Jak si můžete všimnout, tyto data jsou subjektivní a je třeba je ohodnotit a zapsat ručně (časem se zde může objevit i klikátko, pokud si na to vzpomenu).

### Příklad jak připravit data k použití

Facebook má takovou hezkou věc jako kalendář narozenin. Tu si rozklikněte a můžete začít vyplňovat.

**Příklad**:
>*Upozornění: shoda s existujícími osobami je čistě náhodná*

Mí přátelé:
>*Petr Kámen - 12.08. - docela cool týpek, dá se s ním vajbit, ale docela retard  | Vibe: 6/10 Kkt: 7/10*
>
>*Lada Horáková - 24.7. - docela fajn, dokud ji člověk nepozná víc... | Vibe: 3/10 Kkt: 8/10*
> 
>*Alexei Provozov - 22.1. - extrémní míčař, super chábr, lidi ho milujou | Vibe: 10/10 Kkt: 1/10*
> 
>*Jana Stromová - 11.4. - haha moje ex, k tomu se nebudu vyjadřovat | Vibe: 6/10 Kkt: 10/10*
(...)

Nyní je čas přepsat hodnoty do CSV formátu:
>lev;6;7
> 
>lev;3;8
> 
>vodnář;10;1
> 
>býk;6;10
> 
>(...)

Následně uložit do textového souboru a je hotovo. 

## Jak použít skript???
- **Pro lidi, co nechtějí prskat, že jsem debil a hardcodenul tam cestu k souboru**:
-- Přejmenujte texťák s vašimi daty na "xd.txt" a pak stačí spustit "znameniparser.py".

- **Pro lidi, co chtějí prskat, že jsem debil a hardcodenul tam cestu k souboru**:
-- Když jste tak chytří, tak si tu hardcodnutou cestu přepište na cokoli jinýho. A vůbec, kouknu a vidim, ne?
Pokud chcete dělat elitistu, tak nepotřebujete číst dokumentaci, co? :)

# Co mě k tomuhle vedlo?
Netuším, je to produkt rozohněné internetové diskuze a manické epizody, která vyústila v hyperproduktivitu. Jo, taky jsem tenhle branch smazal a ztratil jsem celý kód, díkybohu, že jsem nezavřel okno gitu a měl jsem pořád RSA toho commitu, takže jsem se mohl checkoutnout zpátky.
##
##
##
**EN** 

Sorry english speaking folks, but this tool isn't something, that someone would want to use unironically... 
But if you insist, use google translator, but I warned you. PLEASE DON'T.

