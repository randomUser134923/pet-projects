window.addEventListener('load', function () {
    window.onload = test();
    
    function test() {
        document.body.style.background = "#444444";
        setTimeout(() => document.body.style.background = "", 1000);
    }
});