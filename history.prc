grep "[0-9]" corpus/*.txt.*  | sed 's/+[0-9]/+/g' | sed 's/-[0-9]/-/g' | sed 's/##/*"/g' | sed 's/txt:/txt*/g' | sed 's/corpus[/]//g' | sed 's/Canon G3.txt.A/A/g' | sed 's/Nokia 6610.txt.B/B/g' | sed 's/Nikon coolpix 4300.txt.C/C/g' |  sed 's/Apex AD2600 Progressive-scan DVD player.txt.D/D/g' |  sed 's/Creative Labs Nomad Jukebox Zen Xtra 40GB.txt.E/E/g' | sed 's/:/*/g' | sed 's/ [.]/"/g' | grep -rv ",," | sed 's/,//g' | sed 's/*/,/g' | grep -r "[+-]"


