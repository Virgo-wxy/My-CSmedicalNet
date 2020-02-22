$(function () {
    $(".top-bar>ul>li:gt(1)").hover(function () {
        $(this).children().css("color","#fff");
        $(this).css("background-color","#FF6600");
    },function () {
        $(this).children().css("color","#999");
        $(this).css("background-color","#333");
    });
    $(".top-bar>span>li").hover(function () {
        $(this).children().css("color","#fff");
        $(this).css("background-color","#FF6600");
    },function () {
        $(this).children().css("color","#999");
        $(this).css("background-color","#333");
    });
    //注册和登录页面功能
    $("#user_name").blur(function () {
        var regUsn = /^[a-zA-Z]\w{2,14}$/g;
        content = $(this).val();
        if (content == "") {
            $(this).next("span").text("用户名不能为空");
            $(this).next("span").css("display","block");
        } else {
            if (!regUsn.test(content)) {
                $(this).next("span").text("3到15个英文、数字或下划线，必须字母开头！");
                $(this).next("span").css("display","block");
            } else {
                $(this).next("span").css("display","none");
            }
        }
    });
    $("#pwd").blur(function () {
        var regUsn = /^[a-zA-Z0-9]{6,15}$/g;
        content = $(this).val();
        if (content == "") {
            $(this).next("span").text("密码不能为空");
            $(this).next("span").css("display","block");
        } else {
            if (!regUsn.test(content)) {
                $(this).next("span").text("密码必须是6到15位数字或字母组成！");
                $(this).next("span").css("display","block");
            } else {
                $(this).next("span").css("display","none");
            }
        }
    });
    $("#cpwd").blur(function () {
        pwd = $("#pwd").val();
        cpwd = $(this).val();
        if (pwd != cpwd) {
            $(this).next("span").text("两次输入密码不一致！");
            $(this).next("span").css("display","block");
        } else {
            $(this).next("span").css("display","none");
        }
    });
    $("#email").blur(function () {
        var regUsn = /^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9]{2,6}$/g;
        content = $(this).val();
        if (content == "") {
            $(this).next("span").text("email不能为空");
            $(this).next("span").css("display","block");
        } else {
            if (!regUsn.test(content)) {
                $(this).next("span").text("你输入的邮箱格式不正确！");
                $(this).next("span").css("display","block");
            } else {
                $(this).next("span").css("display","none");
            }
        }
    });
    //确定删除提示
    $(".del").click(function () {
        confirm("确定要删除吗？")
    });
    //确定注册提示
    $("#my_reg").click(function () {
        confirm("确定要注册吗？")
    });
    // 确认添加提示
    $(".add").click(function () {
        confirm("确定要添加吗？")
    });
    // 回复成功提示
    $(".resp").click(function () {
        alert("回复成功！！！")
    });
    // 确认修改提示
    $(".update").click(function () {
        confirm("确定要修改吗？")
    });
});