'use strict'

function ucFirst( name ) {
    if (!name) { return name; }
    
    return name[0].toUpperCase()+name.substr(1);

}


function checkSpam( line , word){
    let target = word.toLowerCase();
    let checkLine = line.toLowerCase();
    return checkLine.includes(target) || checkLine.includes('xxx');
}

function truncate ( str, maxlength ) {
    if ( str.length > maxlength ) {
        //return str.substr(0,maxlength-1) + "..."
        return str.slice(0,maxlength-1) +"..."
    }
    return str;
}

function extractCurrencyValue(str) {
    return +str.slice(1,str.length);
}

function test(){
    console.log( extractCurrencyValue("$120"))  
}

test();