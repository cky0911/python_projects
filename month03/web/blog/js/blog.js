// 针对login页面定义一个对象
var log = {
    startdt: "2023-9-15",
    enddt: "2023-9-15",
    updatedt: "2023-9-15",
    author: "cky"
}
// 由对象派生业务逻辑 中间层
log.submit = {
    // 验证某个值是否为空
    check:function(v){
        var _v = (v == "") ? true : false;
        return _v;
    },
    autoHide:function(obj){
        setTimeout(function(){
            obj.hide();
        }, 2000)
    }
}

// 定义一个验证内容是否为空的函数
function checkValue(){
    // 获取元素对象并保存在变量中
    var $username = $("#username");
    var $password = $("#password");
    var $err1 = $("#err1");
    var $err2 = $("#err2");
    if (!log.submit.check($username.val()) && !log.submit.check($password.val())) {
        return true;
    } else {
        if ($username.val() == "") {
            $err1.show();
            // 2秒后自动隐藏
            log.submit.autoHide($err1);
            // 阻止提交
            return false;
        } else {
            $err2.show();
            // 2秒后自动隐藏
            log.submit.autoHide($err2);
            return false;
        }
    }
}

// 定于一个基于列表页的业务逻辑
var lst = {
    // 标题 图片 副标题 说明
    template:function(t, u, p1, p2){
        var _html = "";
            _html += '<div class="item">';
            _html += '    <div class="title">';
            _html += '        <h3>' + t + '</h3>';
            _html += '    </div>';
            _html += '    <div class="con">';
            _html += '        <div class="cleft">';
            _html += '            <img src="'+ u +'" alt="">';
            _html += '        </div>';
            _html += '        <div class="cright">';
            _html += '            <p class="ptop">';
            _html += '            '+ p1;
            _html += '            </p>';
            _html += '            <p class="pbottom">';
            _html += '            ' + p2;
            _html += '            </p>';
            _html += '        </div>';
            _html += '    </div>';
            _html += '</div>';
        return _html;
    }
}
// 定义一个数组保存需要展示的数据
var arrData = [
                {
                    t: "花间一壶酒，独酌无相亲",
                    u: "images/toppic02.jpg",
                    p1: "举杯邀明月，对影成三人。月既不解饮，影徒随我身。",
                    p2: "大闸蟹 学无止境 2023-09-15 66999已阅读 7777",
                },{
                    t: "送杜少府之任蜀川唐代",
                    u: "images/banner01.jpg",
                    p1: "王勃城阙辅三秦，风烟望五津。与君离别意，同是宦游人。海内存知己，天涯若比邻。无为在歧路，儿女共沾巾。",
                    p2: "小笼包 学无止境 2023-09-15 23333已阅读 6666",
                },{
                    t: "登幽州台歌唐代",
                    u: "images/banner02.jpg",
                    p1: "陈子昂前不见古人，后不见来者。念天地之悠悠，独怆然而涕下。",
                    p2: "小龙虾 学无止境 2023-09-15 76543已阅读 3333",
                }
            ];
for (var i = 0; i < arrData.length; i++) {
    // 通过模板生成新的列表数据
    var _HTML = lst.template(arrData[i].t, arrData[i].u, arrData[i].p1, arrData[i].p2);
    // 追加到列表
    $(".lst").append(_HTML);
}

// 定义一个基于我的相册页的业务逻辑
var pics = {
    template:function(u, n, t){
        var _html = "";
            _html += '<div class="item">';
            _html += '    <div class="imgs">';
            _html += '        <img src="'+ u +'" alt="">';
            _html += '        <div class="tip">喜欢 | '+ n +'</div>';
            _html += '    </div>';
            _html += '    <div class="title">';
            _html += '        <h3>'+ t +'</h3>';
            _html += '    </div>';
            _html += '</div>';
        return _html;
    }
}
// 定义一个数组保存需要展示的数据
var arrPics = [
    {
        u: "images/banner01.jpg",
        n: "888",
        t: "Java相关截图",
    },{
        u: "images/banner02.jpg",
        n: "666",
        t: "C#相关截图",
    },{
        u: "images/banner03.jpg",
        n: "555",
        t: "Golang相关截图",
    }
];
for (var i = 0; i < arrPics.length; i++) {
    // 通过模板生成新的列表数据
    var _HTML = pics.template(arrPics[i].u, arrPics[i].n, arrPics[i].t);
    // 追加到列表
    $("#pics").append(_HTML);
}