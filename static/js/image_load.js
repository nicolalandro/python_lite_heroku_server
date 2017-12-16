$(document).ready(function(){
    init();
});

function init(){
    $('#send_json').click(clickSendImage);
}

function clickSendImage(d){
    var species = $('#fish_specie').val();
    var image = $('#dropzone').find('img').attr('src');
    if(isInputCorrect(species, image)){
        toastSuccess("correct")
    }
}

function isInputCorrect(species, image){
    if( !(species && species.length > 0) ){
        toastError("No species found", "Please insert the specie of fish in image that you load.")
    }
    if( !(image && image.length > 0) ) {
        toastError("No image found", "Please select an image from your computer.")
    }

    return species && species.length > 0 && image && image.length > 0;
}
///////////////////////////////
//       TOAST AREA
///////////////////////////////
function toastSuccess(msg){
    var errorElement = '<div id="error" class="wrapper">';
    errorElement += '<div class="toast-message success">';
    errorElement += '<div class="quote"></div>';
    errorElement += '<a class="close" href="#success">&times;</a>';
    errorElement += '<div class="inner-left">';
    errorElement += '<svg version="1.1" id="icon_success" class="icon" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="48px" height="48px" viewBox="0 0 48 48" enable-background="new 0 0 48 48" xml:space="preserve">';
    errorElement += '<path fill="#fff" d="M24,0C10.745,0,0,10.744,0,24s10.745,24,24,24s24-10.744,24-24S37.255,0,24,0z M21.5,34l-11-11l3.5-3.5l7.5,4.5L35,13.5l3.5,3.5L21.5,34z"/>';
    errorElement += '</svg>';
    errorElement += '</div>';
    errorElement += '<div class="inner-right">';
    errorElement += '<h1>';
    errorElement += 'Success';
    errorElement += '</h1>';
    errorElement += '<p>';
    errorElement += msg;
    errorElement += '</p>';
    errorElement += '</div>';
    errorElement += '</div>';
    errorElement += '</div>';
    $( "body" ).append( errorElement );
    addToastListener();
}

function toastError(title,msg){
    var errorElement = '<div id="error" class="wrapper">';
    errorElement += '<div class="toast-message error">';
    errorElement += '<div class="quote"></div>';
    errorElement += '<a class="close" href="#error">&times;</a>';
    errorElement += '<div class="inner-left">';
    errorElement += '<svg version="1.1" id="error1" class="icon" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="48px" height="48px" viewBox="0 0 48 48" enable-background="new 0 0 48 48" xml:space="preserve">';
    errorElement += '<path fill="#1E2832" d="M24,0C10.744,0,0,10.744,0,24s10.744,24,24,24s24-10.744,24-24S37.256,0,24,0z M36.548,31.952l-4.596,4.596 L24,28.596l-7.952,7.952l-4.596-4.596L19.404,24l-7.952-7.952l4.596-4.597L24,19.404l7.952-7.953l4.596,4.597L28.596,24 L36.548,31.952z"/>';
    errorElement += '</svg>';
    errorElement += '</div>';
    errorElement += '<div class="inner-right">';
    errorElement += '<h1>';
    errorElement += title;
    errorElement += '</h1>';
    errorElement += '<p>';
    errorElement += msg;
    errorElement += '</p>';
    errorElement += '</div>';
    errorElement += '</div>';
    errorElement += '</div>';
    $( "body" ).append( errorElement );
    addToastListener();
}

function addToastListener(){
    var toast = $('.toast-message');
    setTimeout(function() {
        dispose($('.wrapper'));
     }, 10000);
    if(toast.length) {
        toast.find('.close').on('click', function(e) {
            e.preventDefault();
            dispose($(this).closest('.wrapper'))
        });
    }
}

function dispose(el) {
    $.when(el.animate({ 'opacity': 0}, 'slow', function() {
        $(this).slideUp('slow')
     })).done(function() {
        $(this).remove();
     });
  }
