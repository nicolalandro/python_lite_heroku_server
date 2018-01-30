$(document).ready(function(){

    $('.show-list').click(function(){
        $('.wrapper').addClass('list-mode');
    });

    $('.hide-list').click(function(){
        $('.wrapper').removeClass('list-mode');
    });

    $( ".box" ).each(function( index ) {
        var row_data = $( this );
        var name = row_data.attr('namel');
        var size = parseInt(row_data.attr('sizel'));
        console.log( index + ": ajax call for " + name );
        var data = {'name':name, 'size':size};
         $.ajax({
                        url: 			"/api/load_data_from_cloud",
                        type: 			'POST',
                        data: 			JSON.stringify(data),
                        contentType:    "application/json; charset=utf-8",
                        dataType:       "json",
                        complete:       complete,
                        success: 		success,
                        error:          error
                    });
    });

});

function success(data){
    var box = $( ".box[namel='" + data['name'] + "']" );
    var h1 = box.find('.title')
    str = h1.text();
    h1.html(str + ' - ' + data['specie']);
    box.find('img').attr('src', data['img']);
};
function complete(){
    console.log("complete");
};
function error(xhr){
    console.log("Error: " + xhr.status + ", " + xhr.statusText);
};