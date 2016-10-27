$(document).ready(function() {
    //var isFirstTime = true;
    //if (isFirstTime) {
    var url = window.location.href;
    //url = "test";
    //var content = document.getElementById("content");
    //var obj = {content: content};
    var obj = {};
    console.log("Loaded " + url);

    loadURL();
    window.history.replaceState(obj,"title",url);

    var path = window.location.href.indexOf('albumid');
    if (path == -1) {
        var picid = window.location.href.split('picid')[1];
        $('#pic_caption_input').click(function(event) {
                    event.preventDefault();
                    console.log("typed");
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
                            console.log("success");
                            },
                        error : function(response) {
                            console.log("error");
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
                        }

                    });
                });
    }

});

window.onpopstate = function(event) {
    console.log("Reached popstate");
    console.log("Loaded popstate url  " + window.location.href);
    
    loadURL();
    //window.history.replaceState(obj,"title",window.location.href);
};

function loadURL() {
    document.getElementById("content").innerHTML = "";
    console.log("LOADURL CALLED");
    var path = window.location.href.indexOf('albumid');
    var method = "";
    var id = "";
    if (path == -1) {
        method = 'pic';
        var id = window.location.href.split('picid=')[1];
    }
    else {
        method = 'album';
        var id = window.location.href.split('albumid=')[1];
    }

    //url for ajax is decided
    var url = "http://localhost:3000/gu4wdnfe/p3/api/v1/"+method+"/"+id;
    console.log(url);

    //fill page with ajax
    //alert("got here");
    $.ajax({
        type: "GET", 
        //contentType: "application/json; charset=UTF-8",
        //data: JSON.stringify(), 
        url: url,
        success : function(data) {
            if (method == 'album'){
                //alert("success");
                //parse data
                //data = JSON.parse(data);
                var access = data['access']; 
                var albumid = data['albumid'];
                var created = data['created'];
                var lastupdated = data['lastupdated'];
                var photos = data['pics'];
                var title = data['title'];
                var username = data['username'];


                //fill in album and name
                var page_title = document.createElement("h3");
                console.log("title: " + title + " access: " + access + " albumid: " + albumid + " created: " + created
                             + " lastUpdated: " + lastupdated + " photos: " + photos + " username: " + username);
                var album_title = document.createTextNode(title + "-" + username);
                page_title.appendChild(album_title);


                //fill in edit link
                var album_edit = document.createElement("a");
                var link = "http://localhost:3000/gu4wdnfe/p3/album/edit?albumid="+albumid;
                album_edit.href = link;
                album_edit.innerHTML = "EDIT<br>";

                //append album-name and edit link
                var page = document.getElementById("content");
                page.appendChild(page_title);
                page.appendChild(album_edit);

                var newURL = ""

                //fill out photos
                for (i = 0; i < photos.length; i++){
                    //parse photo data
                    //console.log("photo loaded")
                    photo = photos[i];
                    var caption = photo['caption']; 
                    var sequencenum = photo['sequencenum'];
                    var picid = photo['picid'];
                    var format = photo['format'];
                    var date = photo['date'];
                    var albumid = photo['albumid'];
                    //console.log("picidbefore " + picid);


                    //add image and link
                    var parent_element = document.createElement("a");

                    var image_element = document.createElement("IMG");
                    image_element.src = "/static/images/" + picid + "." + format;
                    image_element.width = "200";
                    image_element.height = "200";
                    newURL = "http://localhost:3000/gu4wdnfe/p3/pic?picid=" + picid;
                    parent_element.href = newURL;
                   
                    //TODO: add onlick function to go to next state
                    /*image_element.onclick = function() {
                        window.history.pushState({},"test",window.location.href);
                        //alert(id);
                        //var tempURL = newURL;
                        //var tempURL = this->id;
                        window.history.replaceState({},"pic",newURL);
                        //alert("going to " + newURL);
                        window.history.go(0);
                    }*/

                    //fill in caption data
                    var caption_element = document.createElement("p");
                    var pic_caption = document.createTextNode(caption);
                    caption_element.appendChild(pic_caption);

                    //fill in date data
                    var date_element = document.createElement("h6");
                    var pic_date = document.createTextNode("Date:" + date);
                    date_element.appendChild(pic_date);

                    //append photo, caption, and date
                    parent_element.appendChild(image_element);
                    page.appendChild(parent_element);
                    page.appendChild(caption_element);
                    page.appendChild(date_element);
                }
            }
            

            else if (method == 'pic'){
                //parse pic data
                var albumid = data['albumid'];
                var caption = data['caption'];
                var format = data['format'];
                var next = data['next'];
                var prev = data['prev'];
                var picid = data['picid'];
                console.log("picid loaded is " + picid + " + prev " + next);

                //create image data
                var image_element = document.createElement("IMG");
                image_element.src = "/static/images/" + picid + "." + format;
                image_element.width = "200";
                image_element.height = "200";

                //create caption data
                var caption_element = document.createElement("p");
                var pic_caption = document.createTextNode(caption);
                caption_element.appendChild(pic_caption);

                //create previous data
                var prev_element = document.createElement("h6");
                var prev_pic = document.createTextNode("Previous");
                //append previous
                prev_element.appendChild(prev_pic);
                prev_element.onclick = function() {
                    if (prev == -1) {
                        console.log("Previous returned to same pic");
                        window.history.pushState({},"",window.location.href);
                        var newURL = "http://localhost:3000/gu4wdnfe/p3/pic?picid=" + picid;
                        window.history.replaceState({},"prev",newURL);
                        window.history.go(0);
                    }
                    else {
                        window.history.pushState({},"",window.location.href);
                        var newURL = "http://localhost:3000/gu4wdnfe/p3/pic?picid=" + prev;
                        window.history.replaceState({},"prev",newURL);
                        window.history.go(0);
                    }
                }

                

                //fill out next data
                var next_element = document.createElement("h6");
                var next_pic = document.createTextNode("Next");
                //append next
                next_element.appendChild(next_pic);
                next_element.onclick = function() {
                    if (next == 1){
                        console.log("Next returned to same pic");
                        window.history.pushState({},"",window.location.href);
                        var newURL = "http://localhost:3000/gu4wdnfe/p3/pic?picid=" + picid;
                        window.history.replaceState({},"next",newURL);
                        window.history.go(0);
                    }
                    else {
                        window.history.pushState({},"",window.location.href);
                        var newURL = "http://localhost:3000/gu4wdnfe/p3/pic?picid=" + next;
                        window.history.replaceState({},"next",newURL);
                        window.history.go(0);
                    }
                }


                //create header
                var input_header = document.createElement("h6");
                var header = document.createTextNode("Edit Caption:");

                //append header data to header node
                input_header.appendChild(header);

                //create input for caption
                var caption_input = document.createElement("INPUT");
                caption_input.setAttribute("type", "text");
                caption_input.setAttribute("id", "pic_caption_input")
                var page = document.getElementById("content");
                page.appendChild(image_element);
                var brk = document.createElement("br");
                page.appendChild(brk);
                page.appendChild(caption_input);


                //ajax function for caption added

                //append everything to page
                
                
                page.appendChild(caption_element);
                page.appendChild(prev_element);
                page.appendChild(next_element);
                page.appendChild(input_header);
                
            }

        },
    
        error : function(response) {
            console.log("single page js failed with " + response.responseText);
            var response = JSON.parse(response);
            var code = response.status;
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
}



/*
function onclickFunc(newURL) {
    window.history.pushState({},"test",window.location.href);
    window.history.replaceState({},"pic",newURL);
    window.history.go(0);
}
*/





