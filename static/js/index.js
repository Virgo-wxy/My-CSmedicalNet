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
    // 图片自动切换
    var $Img = $("#imgs>img");
    var $index = $(".index>div");
    ImgIndex=7;
    index=0;
    function auto_Img() {
        if (ImgIndex==0) {
            ImgIndex=7;
            index=0;
        }else{
            ImgIndex--;
            index++;
        }
        $($Img.eq(ImgIndex)).show().siblings().hide();
        $($index.eq(index)).css("border-color","#FF6600").siblings().css("border-color","#cccccc");
    }
    setInterval(auto_Img,3000);
    //图片点击切换
    $(".left>a").click(function () {
        if (ImgIndex==7) {
            ImgIndex=0;
            index=7;
        }else{
            ImgIndex++;
            index--;
        }
        $($Img.eq(ImgIndex)).show().siblings().hide();
        $($index.eq(index)).css("border-color","#FF6600").siblings().css("border-color","#cccccc");
    });
    $(".right>a").click(function () {
        if (ImgIndex==0) {
            ImgIndex=7;
            index=0;
        }else{
            ImgIndex--;
            index++;
        }
        $($Img.eq(ImgIndex)).show().siblings().hide();
        $($index.eq(index)).css("border-color","#FF6600").siblings().css("border-color","#cccccc");
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
    $("#allow").click(function () {
        var checked=$(this).is(":checked");
        if (checked == false) {
            $(this).next().next("span").text("请勾选同意！");
            $(this).next().next("span").css("display","block");
        } else {
            $(this).next().next("span").css("display","none");
        }
    });
    // 留言自动滚动
    var marginTop = 0;
    setInterval(function () {
        $(".all>div>ul>li:first").animate({"margin-top":marginTop--},0,function () {
            var $first = $(this);
            if (!$first.is(":animated()")) {
                if (-marginTop>$first.height()) {
                    $first.css("margin-top","0px").appendTo(".all>div>ul");
                    marginTop = 0;
                }
            }
        });
    },40);
    //
    $(".user").click(function () {
        $(".navbar>ul>li:eq(0)").addClass("current");
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
    // 医院页面
    $(".hospitals>.hospital>.intro").click(function () {
        $(this).next('div').toggle();
    });
    $(".hospitals>.hospital").hover(function () {
        $(this).children(".intro_content").removeClass("pop");
        $(this).children(".intro_content").addClass("po");
    },function () {
        $(this).children(".intro_content").removeClass("po");
        $(this).children(".intro_content").addClass("pop");
    });
    function f() {
        $(".hospital>.intro_content:hidden").parent().removeClass("poop");
        $(".hospital>.intro_content:visible").parent().addClass("poop");
    }
    setInterval(f,1);
    // 人才招聘页面
    $(".details").hover(function () {
        $(this).children().css("display","block");
    },function () {
        $(this).children().css("display","none");
    });
    // 验证码
     $('#mpanel1').slideVerify({
		type : 1,		//类型
		vOffset : 5,	//误差量，根据需求自行调整
		barSize : {
			width : '80%',
			height : '40px',
		},
		ready : function() {
		},
		success : function() {
		},
		error : function() {
		}
      });
});