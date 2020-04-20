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

function GetTexts(obj) {
    var sdata = {
                "xingzuo": $("#xingzuo").val(),
                "method":$('#subButton').attr('data')};
    $.ajax({
        url:"/getText",
  　　  type : "post",
  　　  dataType:"json",
        headers: {
            "Content-Type": "application/json;charset=utf-8"
        },
        contentType:'application/json; charset=utf-8',
        data:JSON.stringify(sdata),
        success:function(data){
            $("#conts").html(data.texts)
        },
        error:function(e){
                alert("error");
        }
    })
}
