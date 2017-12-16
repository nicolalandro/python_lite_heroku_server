$(document).ready(function(){
    init();
});

function init(){
    $('#send_json').click(clickSendImage);
}

function clickSendImage(d){
    console.log("send image...")
    var species = $('#fish_specie').val();
    if(species && species.length > 0){
        console.log(species)
    }
    else {
        console.log("No species found")
    }
}