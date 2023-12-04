proc import datafile="C:\Users\jb4555\AdventOfCode\2023\day2\input.csv"
    out=input
    dbms=csv
    replace;
    getnames=no;
    guessingrows=100;
    delimiter=';';
run;

/*only 12 red cubes, 13 green cubes, and 14 blue cubes*/
data t1;
    retain id;
    set input;
    id=input(substr(var1,6),8.);
    drop var1;
    length _antal 8.;
    re_red=prxparse('/(\d+)\s(red).+/');
    re_green=prxparse('/(\d+)\s(green).+/');
    re_blue=prxparse('/(\d+)\s(blue).+/');
    array ind (6)  var2 var3 var4 var5 var6 var7;

    do i=1 to 6;
        if not missing(ind(i)) then do;
            _antal_red=0;
            _antal_green=0;
            _antal_blue=0;

            if prxmatch(re_red,ind(i)) then do;
                _antal_red=prxposn(re_red, 1, ind(i));
            end;

            if prxmatch(re_green,ind(i)) then do;
                _antal_green=prxposn(re_green, 1, ind(i));
            end;

            if prxmatch(re_blue,ind(i)) then do;
                _antal_blue=prxposn(re_blue, 1, ind(i));
            end;

            if _antal_red<=12 and _antal_green<=13 and _antal_blue<=14 then do;
                valid=1;
            end;
            else do;
                valid=0;
                invalidGame=ind(i);
                leave;
            end;
        end;
    end;

    /*where var1='Game 16';*/
run;

proc means data=t1 sum;
    var id;
    where valid = 1;
run;

data t1;
    retain id;
    set input;
    id=input(substr(var1,6),8.);
    drop var1;
    length _antal 8.;
    re_red=prxparse('/(\d+)\s+(red)/');
    re_green=prxparse('/(\d+)\s+(green)/');
    re_blue=prxparse('/(\d+)\s+(blue)/');
    array ind (6)  var2 var3 var4 var5 var6 var7;

    do i=1 to 6;
        if not missing(ind(i)) then do;
            _antal_red=0;
            _antal_green=0;
            _antal_blue=0;

            if prxmatch(re_red,ind(i)) then do;
                _antal_red=prxposn(re_red, 1, ind(i));
                max_red=max(_antal_red,max_red);
            end;

            if prxmatch(re_green,ind(i)) then do;
                _antal_green=prxposn(re_green, 1, ind(i));
                max_green=max(_antal_green,max_green);
            end;

            if prxmatch(re_blue,ind(i)) then do;
                _antal_blue=prxposn(re_blue, 1, ind(i));
                max_blue=max(_antal_blue,max_blue);
            end;
        end;
    end;

    power=max_red*max_green*max_blue;
/*    where var1='Game 12';*/
run;

proc means data=t1 sum;
    var power;

    /*    where valid = 1;*/
run;