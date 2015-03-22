$("#download_button").click( function()
    {
        var width = $( "#dim_w" ).val();
        var height = $( "#dim_h" ).val();
        var flagName = $('#resize_image').attr("alt").replace(' ', '_') + "." + $('input[type="radio"][name="optradio"]:checked').val();
        console.log('Download: ' + width + "," + height + "," + flagName);
        $(this).attr("href","/generate/" + width + "/" + height + "/" + flagName);
   }
);

$(document).on('show.bs.modal', function(e) {
    var flagName = $(e.relatedTarget).data('flag-name');
    var flagFile = $(e.relatedTarget).data('flag-file');
    var fsp = flagFile.split('_');
    fsp[1] = parseInt(fsp[1], 10);
    fsp[2] = parseInt(fsp[2], 10)
    
    $(function() {
        $( "#resizable" ).resizable({
            aspectRatio: fsp[1]/fsp[2],
            minWidth: 16,
            containment: "#container",
            resize: function(e, ui) {
                $( "#dim_w" ).val(Math.round(ui.size.width*2));
                $( "#dim_h" ).val(Math.round(ui.size.height*2));
            },
            start: function(e, ui) {
                $( "#dim_w" ).val(Math.round(ui.size.width*2));
                $( "#dim_h" ).val(Math.round(ui.size.height*2));
            },
            stop: function(e, ui) {
                $( "#dim_w" ).val(Math.round(ui.size.width*2));
                $( "#dim_h" ).val(Math.round(ui.size.height*2));
            }
        });
    });
    
    var container_borders = $( "#container" ).css([ "borderTopWidth", "borderRightWidth", "borderBottomWidth", "borderLeftWidth" ]);
    var container_padding = $( "#container" ).css([ "paddingTop", "paddingRight", "paddingBottom", "paddingLeft" ]);
    var resizable_borders = $( "#resizable" ).css([ "borderTopWidth", "borderRightWidth", "borderBottomWidth", "borderLeftWidth" ]);
    var resizable_padding = $( "#resizable" ).css([ "paddingTop", "paddingRight", "paddingBottom", "paddingLeft" ]);

    var container_width  = fsp[1]*3 + parseInt(container_borders.borderLeftWidth.replace('px', ''), 10) + 
                                      
                                      parseInt(resizable_borders.borderLeftWidth.replace('px', ''), 10) +
                                      parseInt(resizable_borders.borderRightWidth.replace('px', ''), 10) + 
                                      parseInt(resizable_padding.paddingLeft.replace('px', ''), 10) + 
                                      parseInt(resizable_padding.paddingRight.replace('px', ''), 10) + 1;
                                           
    var container_height = fsp[2]*3 + parseInt(container_borders.borderTopWidth.replace('px', ''), 10) + 
                                      
                                      parseInt(resizable_borders.borderTopWidth.replace('px', ''), 10) +
                                      parseInt(resizable_borders.borderBottomWidth.replace('px', ''), 10) + 
                                      parseInt(resizable_padding.paddingTop.replace('px', ''), 10) + 
                                      parseInt(resizable_padding.paddingBottom.replace('px', ''), 10) + 1;
                                           
    var resizable_width  = fsp[1] + parseInt(resizable_borders.borderLeftWidth.replace('px', ''), 10) +
                                    parseInt(resizable_borders.borderRightWidth.replace('px', ''), 10) ;
                                           
    var resizable_height = fsp[2] + parseInt(resizable_borders.borderTopWidth.replace('px', ''), 10) +
                                    parseInt(resizable_borders.borderBottomWidth.replace('px', ''), 10) ;                                       
    
    console.log("Container Borders: " + JSON.stringify(container_borders));
    console.log("Container Padding: " + JSON.stringify(container_padding));
    console.log("Resizable Borders: " + JSON.stringify(resizable_borders));
    console.log("Resizable Padding: " + JSON.stringify(resizable_padding));            
    console.log( "Page Ready: " + fsp[1] + "," + fsp[2] + ", " + 
                 container_width + "," + container_height + ", " + resizable_width + "," + resizable_height);

    $('#modal-title').text(flagName +': Drag corner to resize flag.'); 
    $('#resize_image').attr("alt", flagName);
    $('#resize_image').attr("src", 'images/us/svg/' + flagFile);
    $('#container').width(container_width);
    $('#container').height(container_height);
    $('#resizable').width(resizable_width);
    $('#resizable').height(resizable_height);
    
    $( "#dim_w" ).val(fsp[1]*2);
    $( "#dim_h" ).val(fsp[2]*2);
}); 