var language;
var map;

$(document).ready(function() {
    language = $('html').attr('lang');

    if ($("div#map").length) {
        create_address_search();

        map = L.map('map').setView([50.84331852979277,4.357895514064874], 16);
        var nexrad = L.tileLayer.wms("http://geoserver.gis.irisnet.be/urbis/wms/gwc", {
            layers: 'urbisFR',
            format: 'image/png',
            transparent: true,
            attribution: "CIRB © 2013 ",
        });

        map.addLayer(nexrad);
    }

});

function create_address_search(){
    $('<form id="address_form"><input type="text" id="address" /><input type="submit" value="submit" /></form><div class="result"></div>').insertAfter('div#map');
    $('form#address_form').submit(function(){
        address_value = $('#address').val();
        search_address(address_value);
        return false;
    });

}

function search_address(address){
    search_address_url = 'http://service.gis.irisnet.be/urbis/Rest/Localize/getaddresses';
    $.get(search_address_url, {language: language, address: address, spatialReference: 4326}, function(data){
        $('.result').html(data);
        parsed = jQuery.parseJSON(data);
        result = parsed.result;
        return_point = [result[0].point.y, result[0].point.x];
        return_address = result[0].address.street.name
        map.setView(return_point, 16);
        L.marker(return_point).addTo(map).bindPopup(return_address).openPopup();
    });
}
