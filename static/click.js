function clicks(){
    // console.log("123");
    sendData = {'user':'admin'};
    $.ajax({
        url:"updatebg",
        type:"post",
        data:sendData,
        dataType: 'json',
        processData:false,
        contentType:false,
        success:function(data){
                // $(img_url_new).attr("src",data.img_url_new);
                // $(imgPic).attr("src",data.img_url_new);
            $('#topdiv').css("background",data.colors);
            // console.log(456);
        },
        error:function(e){
                alert("error");
        }
    })
}