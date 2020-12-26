

const prompt = require('prompt');

q3();

function q1() {

    prompt.start();
    
    prompt.get(['input1', 'input2'], function (err, result) {
        if (err) { return onErr(err); }
    
        let input3 = parseInt(result.input1) + parseInt(result.input2)
        console.log(input3);
        
    });
    
    function onErr(err) {
        console.log(err);
        return 1;
    }
}

function q2() {
    console.log( (1.35*10).toFixed()/10 );
    console.log( (6.35*10).toFixed()/10 );
}


function q3() {
    let valid = false;
    initiatePrompt();
    function initiatePrompt() {
        prompt.get(['input1'], function (err, result) {
            if (err) { return onErr(err); }
            if ( isFinite(result.input1) ) {
                console.log(result.input1);
            }
            else {
                initiatePrompt();
            }
        });
    } 
    
    function onErr(err) {
        console.log(err);
        return 1;
    }    
}