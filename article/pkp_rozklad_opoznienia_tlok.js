<script type="text/javascript">

        var OdczytDanych = false;
        var oOdjazd = true;
        var oStPocz = '';
        var oStKon = '';
        var oData = '04.11.2018';
        var oGodzina = '09:49';
        var oCzasPrz = '10';
        var oBezp = false;
        var oStacjePos = [];
        var oSrTrans = [['AG','aglomeracyjny'],['DA','dalekobieżny'],['LO','lokalny'],['SZ','szybki']];
        var oUslugi = [];
        var oPrzew = [['AR','Arriva RP sp. z o.o.','pl-PL'],['CARGO','PKP CARGO SA','pl-PL'],['IC','„PKP Intercity” Spółka Akcyjna','pl-PL'],['KD','Koleje Dolnośląskie S.A.','pl-PL'],['KM','&#34;Koleje Mazowieckie - KM&#34; sp. z o.o.','pl-PL'],['KMŁ','„Koleje Małopolskie” sp. z o.o.','pl-PL'],['KS','Koleje Śląskie sp. z o.o.','pl-PL'],['KW','Koleje Wielkopolskie Sp. z o.o.','pl-PL'],['LEO','LEO Express Global a.s. ','pl-PL'],['ŁKA','„Łódzka Kolej Aglomeracyjna” sp. z o.o.','pl-PL'],['ODEG','Ostdeutsche Eisenbahn GmbH','de-DE'],['PR','&#34;Przewozy Regionalne&#34; sp. z o.o.','pl-PL'],['SKM','Szybka Kolej Miejska ','pl-PL'],['SKMT','PKP Szybka Kolej Miejska w Trójmieście sp. z o.o.','pl-PL'],['SKPL','SKPL Cargo Sp. z o.o.','pl-PL']];

        var KatSz = [['AG','aglomeracyjny'],['DA','dalekobieżny'],['LO','lokalny'],['SZ','szybki']];
        var Uslug = [['AKZ1','zastępcza komunikacja autobusowa'],['ASZ','autobus szynowy'],['BABP','dostępne miejsce do przewijania dziecka'],['BABY1','przedział dla podróżnych z małymi dziećmi'],['BAGD','wagon z miejscem na duży bagaż'],['BILA','biletomat w pociągu'],['BILSL','bilety na przejazd na odcinkach krajowych w wagonie &#34;Sleeperette&#34;, tylko u obsługi pociągu, w miarę wolnych miejsc'],['BRAK','przewoźnik nie zdefiniował usług'],['CATE1','sprzedaż napojów i przekąsek z wózka minibar'],['CISZA','wydzielona strefa ciszy'],['EZT','jednostki elektryczne'],['INWA1','wagon z miejscami dla osób na wózkach - z windą/rampą'],['INWR1','wagon z miejscami dla osób na wózkach - bez windy/rampy'],['K1WAG','1 klasa'],['K2WAG','2 klasa'],['KLIMA','klimatyzacja'],['KOND','przewóz przesyłek konduktorskich'],['KWO2','tylko 2 klasa'],['LOT','połączenie z lotniskiem'],['MENA','przedział menedżerski'],['MIS1','wagon z miejscem zabaw dla dzieci'],['NIEW','wagon z oznaczeniami w alfabecie Braille\'a'],['REZF','rezerwacja miejsc fakultatywna'],['REZF1','fakultatywna rezerwacja w 1 klasie'],['REZM1','rezerwacja miejsc'],['REZO','rezerwacja obowiązkowa'],['ROW2','rezerwacja miejsc w 1 klasie'],['ROWN1','możliwość przewozu rowerów w wagonie nieprzystosowanym do ich przewozu – liczba miejsc ograniczona'],['ROWT1','wagon przystosowany do przewozu rowerów - liczba miejsc ograniczona'],['SLEEP','wagon typu &#34;Sleeperette&#34;'],['US1','wagon gastronomiczny'],['WBEZ1','przełączanie wagonów do innego pociągu'],['WIFI1','dostęp do WiFi'],['WLEZ','wagon z miejscami do leżenia'],['WLEZ2','wagon z miejscami do leżenia dla osób na wózkach - z windą/rampą'],['WSTN','pociag nie zatrzymuje się na wszystkich stacjach'],['WSYP','wagon sypialny'],['WSYP2','wagon z miejscami sypialnymi dla osób na wózkach - z windą/rampą']];
        var Przew = [['AR','Arriva RP sp. z o.o.','pl-PL'],['CARGO','PKP CARGO SA','pl-PL'],['IC','„PKP Intercity” Spółka Akcyjna','pl-PL'],['KD','Koleje Dolnośląskie S.A.','pl-PL'],['KM','&#34;Koleje Mazowieckie - KM&#34; sp. z o.o.','pl-PL'],['KMŁ','„Koleje Małopolskie” sp. z o.o.','pl-PL'],['KS','Koleje Śląskie sp. z o.o.','pl-PL'],['KW','Koleje Wielkopolskie Sp. z o.o.','pl-PL'],['LEO','LEO Express Global a.s. ','pl-PL'],['ŁKA','„Łódzka Kolej Aglomeracyjna” sp. z o.o.','pl-PL'],['ODEG','Ostdeutsche Eisenbahn GmbH','de-DE'],['PR','&#34;Przewozy Regionalne&#34; sp. z o.o.','pl-PL'],['SKM','Szybka Kolej Miejska ','pl-PL'],['SKMT','PKP Szybka Kolej Miejska w Trójmieście sp. z o.o.','pl-PL'],['SKPL','SKPL Cargo Sp. z o.o.','pl-PL']];
        var DCP = '10';
        var CTT = '2018-11-04T09:49:44';
        var CTK = ['2018-12-09T00:00:00', '2019-03-10T00:00:00', '2019-06-09T00:00:00', '2019-09-01T00:00:00', '2019-10-20T00:00:00'];
        var CTZ = ['2018-11-17T00:00:00', '2019-02-16T00:00:00', '2019-05-18T00:00:00', '2019-08-10T00:00:00', '2019-09-28T00:00:00'];

        var urlSearchConnections = '/Wyszukiwarka/WyszukajPolaczenia';
        var urlSearchFastConnections = '/Wyszukiwarka/WyszukajSzybkiePolaczenia';
        var urlSearchResults = '/WynikiWyszukiwania';
        var urlSearchFastResults = '/WynikiWyszukiwania/SzybkiePolaczenia';

        var _Etk = {
            'minSwT': 'Minimalny czas przesiadki',
            'clNewConn': 'Kliknij by dodać nowe połączenie',
            'selXfY': 'Wybrano {x} z {y}',
            'srch': 'Trwa wyszukiwanie połączeń',
            'noCrit': 'Brak zapamiętanych kryteriów wyszukiwania',
            'lstMT': 'Usuń z listy dopuszczalnych środków transportu element: {item}.',
            'lstPR': 'Usuń z listy wymaganych preferencji element: {item}.',
            'lstCR': 'Usuń z listy dopuszczalnych przewoźnika element: {item}.',
            'del': 'Usuń',
            'minMdT': 'Minimalny czas pobytu na stacji pośredniej',
            'lbStFr': 'Wyjazd z',
            'lbStTo': 'Przyjazd do',
            'lbStVi': 'Stacja pośrednia',
            'lbDate': 'Data',
            'lbTime': 'Godzina',
            'lbMoft': 'Środki transportu',
            'lbCarr': 'Przewoźnicy',
            'cthTx1': 'Wybrany termin podróży jest późniejszy, niż data korekty rozkładu jazdy, która jest zaplanowana na {data_korekta}r.',
            'cthTx2': 'Dane, które zostaną zaprezentowane w wynikach wyszukiwania mogą ulec zmianie.',
            'cthTx3': 'Prosimy o ponowne sprawdzenie i zweryfikowanie połączenia po {data_zaplanowanie}r.'
        };

        var _Art = {
			'pAsoV': 'Wyświetlono panel dodatkowych opcji wyszukiwania.',
			'pAsoH': 'Ukryto panel dodatkowych opcji wyszukiwania.',
			'lcDa': 'Usunięto wszystkie zapamiętane kryteria wyszukiwania.',
			'lcCw': 'Zamknięto okno zapisanych kryteriów wyszukiwania.',
			'lcD': 'Usunięto zapamiętane kryteria wyszukiwania.',
			'lcR': 'Wczytano zapamiętane kryteria wyszukiwania.',
			'stSw': 'Zamieniono stacje początkową i końcową.',
			'msA': 'Dodano nowy panel konfiguracji stacji pośredniej.',
			'msD': 'Usunięto stację pośrednią.',
			'ttSa': 'Zazaczono wszystkie dopuszczalne środki transportu.',
			'ttUa': 'Odznaczono wszystkie dopuszczalne środki transportu.',
			'ttCw': 'Zamknięto okno konfiguracji dopuszczalnych środków transportu.',
			'ttD': 'Usunięto środek transportu.',
			'ttDa': 'Wyczyszczono listę dopuszczalnych środków transportu.',
			'pSa': 'Zazaczono wszystkie wymagane udogodnienia.',
			'pUa': 'Odznaczono wszystkie wymagane udogodnienia.',
			'pCw': 'Zamknięto okno konfiguracji wymaganych udogodnień.',
			'pD': 'Usunięto udogodnienie.',
			'pDa': 'Wyczyszczono listę wymaganych udogodnień.',
			'cSa': 'Zazaczono wszystkich dopuszczalnych przewoźników.',
			'cUa': 'Odznaczono wszystkich dopuszczalnych przewoźników.',
			'cCw': 'Zamknięto okno konfiguracji dopuszczalnych przewoźników.',
			'cD': 'Usunięto przewoźnika.',
			'cDa': 'Wyczyszczono listę dopuszczalnych przewoźników.',
			'fcUp': 'Przesunięto szybkie połączenie w górę.',
			'fcDn': 'Przesunięto szybkie połączenie w dół.',
			'fcD': 'Usunięto szybkie połączenie.',
			'fcDa': 'Usunięto wszystkie szybkie połączenia.',
			'fcAp': 'Dodano nowy panel konfiguracji szybkiego połączenia.',
			'fcCw': 'Zapisano i zamknięto okno konfiguracji szybkich połączeń.'
        };
    </script>