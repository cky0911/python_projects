function createXhr() {
    if (window.XMLHttpRequest) {
      // 支持 XMLHttpRequest
      return new XMLHttpRequest();
    } else {
      // 不支持XMLHttpRequest,使用 ActiveXObject 创建异步对象
      return new ActiveXObject("Microsoft.XMLHTTP");
    }
}