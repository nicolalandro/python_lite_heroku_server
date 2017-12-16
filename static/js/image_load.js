$(document).ready(function(){
    init();
});

function init(){
    $('#send_json').click(clickSendImage);
}

function clickSendImage(d){
    console.log("send image...")
    var species = $('#fish_specie').val();
    var image = $('#dropzone').find('img').attr('src');
    if(isInputCorrect(species, image)){
        toastSuccess("correct")
    }
}

function isInputCorrect(species, image){
    if( !(species && species.length > 0) ){
        toastError("No species found")
    }
    if( !(image && image.length > 0) ) {
        toastError("No image found")
    }

    return species && species.length > 0 && image && image.length > 0;
}

function toastSuccess(msg){
    console.log(msg)
}

function toastError(msg){
    console.log(msg)
}
