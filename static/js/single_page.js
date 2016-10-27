$(document).ready(function() {

    //returns -1 if string not found
    var path = window.location.href.indexOf('albumid');
    var method = 'album';
    if (path == -1) {
        method = 'pic';
    }

    var id = window.location.href.split('=')[1];

    $.ajax({
        type: "GET", 
        contentType: "application/json; charset=UTF-8",
        data: JSON.stringify(), 
        url: "http://localhost:3000/gu4wdnfe/p3/api/v1/"+method,
        success : function(data) {

            if (method == 'album'){

                var access = data['access']; 
                var albumid = data['albumid'];
                var created = data['created'];
                var lastupdated = data['lastupdated'];
                var photos = data['pics'];
                var title = data['title'];
                var username = data['username'];


                var page_title = document.createElement("h3");
                var album_title = document.createTextNode(title + "-" + username);
                page_title.appendChild(album_title);


                var album_edit = document.createElement("LINK");
                var edit_link = document.createTextNode("/gu4wdnfe/p3/album/edit?albumid="+albumid);
                album_edit.appendChild(edit_link);


                var page = document.getElementById("content");
                page.appendChild(page_title);
                page.appendChild(album_edit);

                for (i = 0; i < photos.length; i++){

                    var caption = photo['caption']; 
                    var sequencenum = photo['sequencenum'];
                    var picid = photo['picid'];
                    var format = photo['format'];
                    var date = photo['date'];
                    var albumid = photo['albumid'];

                    var image_element = document.createElement("IMG");
                    image_element.src = "/static/images/" + picid + "." + format;
                    image_element.width = "200";
                    image_element.height = "200";
                    image_element.onClick = window.open("/gu4wdnfe/p3/pic?picid=" + picid);

                    var caption_element = document.createElement("p");
                    var pic_caption = document.createTextNode(caption);
                    caption_element.appendChild(pic_caption);

                    var date_element = document.createElement("h6");
                    var pic_date = document.createTextNode("Date:" + date);
                    date_element.appendChild(date);

                    page.appendChild(image_element);
                    page.appendChild(caption_element);
                    page.appendChild(date_element);
                    }
                }
            

            else if (method == 'pic'){
                var albumid = data['albumid'];
                var caption = data['caption'];
                var format = data['format'];
                var next = data['next'];
                var prev = data['prev'];
                var picid = data['picid'];




                var image_element = document.createElement("IMG");
                image_element.src = "/static/images/" + picid + "." + format;

                var caption_element = document.createElement("p");
                var pic_caption = document.createTextNode(caption);
                caption_element.appendChild(pic_caption);

                var prev_element = document.createElement("h6");
                var prev_pic = document.createTextNode("Previous");
                prev_pic.onClick = window.open("/gu4wdnfe/p3/pic?picid=" + prev);
                prev_element.appendChild(prev_pic);

                var next_element = document.createElement("h6");
                var next_pic = document.createTextNode("Next");
                next_pic.onClick = window.open("/gu4wdnfe/p3/pic?picid=" + next);
                next_element.appendChild(next_pic);


                if (next == 1){
                    next_pic.onClick = window.open("/gu4wdnfe/p3/pic?picid=" + picid);
                }
                if (prev == -1){
                    prev_pic.onClick = window.open("/gu4wdnfe/p3/pic?picid=" + picid);
                }


                var input_header = document.createElement("h6");
                var header = document.createTextNode("Edit Caption:");
                input_header.appendChild(header);

                var caption_input = document.createElement("INPUT");
                caption_input.setAttribute("type", "text");
                caption_input.setAttribute("id", "pic_caption_input")


                document.getElementById("pic_caption_input").onkeypressed = function() {
                    $.ajax({
                        type: "PUT", 
                        contentType: "application/json; charset=UTF-8",
                        data: JSON.stringify({                            
                            "caption": caption, 
                            "picid": picid, 
                            "format": format, 
                            "albumid": albumid, 
                            "next": next, 
                            "prev": prev
                        }), 
                        url: "http://localhost:3000/gu4wdnfe/p3/api/v1/pic/"+picid,
                        success : function(data) {
                            },
                        error : function(response) {
                            var response = JSON.parse(response);
                            var my_errors = response['errors'];
                            var error_message = "";
                            var page = document.getElementById("content");

                            for (i = 0; i < my_errors.length; i++){
                                error_message = my_errors[i]['message'];

                                var error_para = document.createElement("p");
                                error_para.setAttribute("class", "error");
                                var error = document.createTextNode(error_message);
                                error_para.appendChild(error);
                                page.appendChild(error_para);
                            }
                    });
                }

                page.appendChild(image_element);
                page.appendChild(caption_element);
                page.appendChild(prev_element);
                page.appendChild(next_element);
                page.appendChild(input_header);
                page.appendChild(caption_input);


            }
        }



    },
        error : function(response) {
            var code = response.status;
            var response = JSON.parse(response);
            var my_errors = response['errors'];
            var error_message = "";
            var page = document.getElementById("content");

            if (code == 403){
                error_message = my_errors['message'];
                var error_para = document.createElement("p");
                error_para.setAttribute("class", "error");
                var error = document.createTextNode(error_message);
                error_para.appendChild(error);
                page.appendChild(error_para);
            }        
        }
    });
});















