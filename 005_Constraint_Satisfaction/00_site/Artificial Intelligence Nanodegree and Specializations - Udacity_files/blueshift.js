!function(){var e=("https:"===document.location.protocol?"https:":"http:")+"//api.getblueshift.com/",t=e+"unity.gif",n=e+"cookiejar.json",o=("https:"===document.location.protocol?"https:":"http:")+"//ib.adnxs.com/getuid?",r=!1,i=!1,a=!1,s="undefined"!=typeof XMLHttpRequest&&"withCredentials"in new XMLHttpRequest;var c,u={eventApiKey:void 0,userParams:{},slots:[],slotParams:{},tz:(new Date).getTimezoneOffset()};function d(e,t){t.tz=u.tz;var n={x:u.eventApiKey,slot:e,user:u.userParams,context:t};return"true"==function(e){var t=window.location.href;e=e.replace(/[\[\]]/g,"\\$&");var n=new RegExp("[?&]"+e+"(=([^&#]*)|&|#|$)").exec(t);return n?n[2]?decodeURIComponent(n[2].replace(/\+/g," ")):"":null}("dev")&&(n.dev=!0),JSON.stringify(n)}function f(t){!function(){u.slots=[];for(var e=document.querySelectorAll("[data-bsft-slot]"),t=0;t<e.length;t++)u.slots.push({name:e[t].dataset.bsftSlot,el:e[t]})}(),u.slotParams=t||{},function(){for(var t=[],n=0;n<u.slots.length;n++)!function(n){t[n]=w(),t[n].open("POST",e+"live",!0),t[n].setRequestHeader("Content-Type","application/json"),t[n].onreadystatechange=function(){if(4===t[n].readyState&&200==t[n].status){try{var e=JSON.parse(t[n].responseText)}catch(e){console.log("error loading slot",e)}e&&e.show&&(o=u.slots[n].el,r=e.width,i=e.height,a=e.content,s=document.createElement("iframe"),o.innerHTML="",o.appendChild(s),s.src="javascript:''",s.style.width=r,s.style.height=i,s.style.border="none",s.contentWindow.document.open(),s.contentWindow.document.write(a),s.contentWindow.document.close(),o.style.width=r,o.style.height=i,o.style.display="block")}var o,r,i,a,s},t[n].send(d(u.slots[n].name,u.slotParams[u.slots[n].name]||{}))}(n)}()}function l(e,t){var n=document.getElementById(e);_(n,"change",function(){N({0:"icapture",1:t,2:document.getElementById(e).value})},!1)}function p(e){new Image(1,1).src=e}function h(e){try{if(null!=y("_bs_fb_pushed"))return;request=n+"?x="+window._blueshiftid+"&k="+e;var t=w();t.open("GET",request,!0),t.onreadystatechange=function(){4==t.readyState&&200==t.status&&function(e){if(function(e){for(var t in e)if(e.hasOwnProperty(t))return!1;return!0}(e))return!0;window._fbq=window._fbq||[],window._fbq.push(["track","user_attributes",e]),m("_bs_fb_pushed","1",1)}(JSON.parse(t.responseText))},t.send(request)}catch(e){}}function w(){if(window.XMLHttpRequest)try{var e=new XMLHttpRequest}catch(t){e=new window.ActiveXObject("Microsoft.XMLHTTP")}return e}function m(e,t,n){var o=new Date;o.setDate(o.getDate()+n);var r=window.location.hostname,i=r.split(".");4==i.length&&i[0]>=0&&i[0]<=255&&i[1]>=0&&i[1]<=255&&i[2]>=0&&i[2]<=255&&i[3]>=0&&i[3]<=255||(r="."+r.replace(/^www./,""));var a=escape(t)+(null==n?"":";expires="+o.toUTCString())+";path=/;domain="+r;document.cookie=e+"="+a}function y(e){var t,n,o,r=document.cookie.split(";");for(t=0;t<r.length;t++)if(n=r[t].substr(0,r[t].indexOf("=")),o=r[t].substr(r[t].indexOf("=")+1),(n=n.replace(/^\s+|\s+$/g,""))==e)return unescape(o)}function g(e){var n,r,c=e[0],d=function(){var e="";try{e=window.top.document.referrer}catch(t){if(window.parent)try{e=window.parent.document.referrer}catch(t){e=""}}return""===e&&(e=document.referrer),e}(),f=Math.floor(1e6*Math.random()+1),g=Math.round(new Date/1e3),b=y("_bs");if("object"==typeof analytics&&"function"==typeof analytics.user&&(n=_blueshiftid,"YmU3MGIwNGVkMzUyZDAzYjA5NDc5NmJjNWZjZTdiMDU="!==(r=btoa(n))&&"MWM2ZGEyNGExOGM1MjQyNTNlZTExNmU0YzUzOTNjZWY="!==r)){var k=analytics.user().anonymousId();b!=k&&m("_bs",k,365),b=k}if(null==b&&m("_bs",b=function(){function e(){return Math.floor(65536*(1+Math.random())).toString(16).substring(1)}return e()+e()+"-"+e()+"-"+e()+"-"+e()+"-"+e()+e()+e()}(),365),"config"==c&&e[1])return e[1].trackClicks&&_(document,"click",function(e){e=e||window.event,element=e.target||e.srcElement,element.href&&N(["click",{p:function(e){for(var t=[];null!=e.parentNode;){for(var n=0,o=0,r=0;r<e.parentNode.childNodes.length;r++){var i=e.parentNode.childNodes[r];i.nodeName==e.nodeName&&(i===e&&(o=n),n++)}""!=e.id?t.unshift(e.nodeName.toLowerCase()+"#"+e.id):n>1?t.unshift(e.nodeName.toLowerCase()+"["+o+"]"):t.unshift(e.nodeName.toLowerCase()),e=e.parentNode}return t}(element).toString(),c:element.href,a:element.innerHTML}])}),!0;if("identify"==c&&(u.userParams=e[1]||{},u.userParams.cookie=b),"track"==c)c=e[1],e=e[2];else{if("capture"==c)return l(e[1],e[2]),!0;if("retarget"==c)return req=o+t+"?t="+g+"&e=appnexus&z="+f+"&x="+window._blueshiftid+"&k="+b+"&appnexus_id=$UID&u="+encodeURIComponent(encodeURIComponent(window.location.href))+"&r="+encodeURIComponent(encodeURIComponent(d)),p(req),!0;if("facebook"==c)return a=!0,!0;"icapture"==c?(c="capture",x=e[1],value=e[2],(e={})[x]=value):e=e[1]}for(var x in req=t+"?t="+g+"&e="+c+"&r="+encodeURIComponent(d)+"&z="+f+"&x="+window._blueshiftid+"&k="+b+"&u="+encodeURIComponent(window.location.href),e)v=e[x],"object"==typeof v?req+="&"+x+"_json="+encodeURIComponent(JSON.stringify(v)):req+="&"+x+"="+encodeURIComponent(v);return s?function(e){try{xhr=w(),xhr.open("GET",e,!0),xhr.send(e)}catch(e){}}(req):p(req),1==a&&"pageload"==c&&h(b),1==i&&"pageload"==c&&(req=o+t+"?t="+g+"&e=appnexus&z="+f+"&x="+window._blueshiftid+"&k="+b+"&appnexus_id=$UID&u="+encodeURIComponent(encodeURIComponent(window.location.href))+"&r="+encodeURIComponent(encodeURIComponent(d)),p(req)),1==a&&"pageload"==c&&h(b),!0}function b(e,t){setTimeout(function(){N(e)},t)}function N(e){if(null!=e[0])if(r)if("identify"!==e[0])if(u.userParams.cookie||new Date-c>1e3)switch(e[0]){case"live":f(e[1]);break;default:g(e)}else b(e,20);else g(e);else b(e,20)}function k(){r=!0,c=new Date,u.eventApiKey=_blueshiftid}if("object"==typeof blueshift){var x=void 0===blueshift.slice?[]:blueshift.slice(0);for(blueshift={events:[],load:function(){k()},capture:function(e,t){l(e,t)},retarget:function(){N(["retarget"])},facebook:function(){N(["facebook"])},track:function(e,t){N(["track",e,t])},pageload:function(e){N(["pageload",e])},identify:function(e){N(["identify",e])},live:function(e){N(["live",e])}},q=0;q<x.length;q++)blueshift.events.push(x[q])}if(document.addEventListener)var _=function(e,t,n){e.addEventListener(t,n,!1)};else _=function(e,t,n){e.attachEvent("on"+t,n)};for(var q=0;q<blueshift.events.length;q++)N(blueshift.events[q]);"complete"===document.readyState?k():window.addEventListener?window.addEventListener("load",k,!1):window.attachEvent&&window.attachEvent("onload",k)}();