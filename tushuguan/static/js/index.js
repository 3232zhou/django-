// $(document).ready(function () {
//    $("table #table tr").bind("click",function () {
//        console.log("xxxx");
//         $(this).remove();
//    })
// });
$(function(){
    $("#table tr").click(function() {
        var t = document.getElementById("table");
        if ($(t.childElementCount)){
                 $(this).remove();
        }else {
             $(this).remove();
        }
    });
});