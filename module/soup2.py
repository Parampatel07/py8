# font-16 color-blue short-nm
from bs4 import BeautifulSoup

html_document = '''<!DOCTYPE html>
<html  lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <meta http-equiv="content-language" content="en" />
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <title>Petrol Price in Bhavnagar Today | Check Bhavnagar Petrol Rates (30th January 2024) - NDTV</title>
        <meta name="description" content="Today's Bhavnagar Petrol Price is 97.77 rupee per litre: Here you can find Latest Petrol/Diesel Price in Bhavnagar city." />
        <meta name="keywords" content="Bhavnagar Petrol price, Bhavnagar Petrol rate, Petrol price in Bhavnagar, todays bhavnagar Petrol price, Todays Petrol price in Bhavnagar" />
        <meta property="og:title" content="Petrol Price in Bhavnagar Today | Check Bhavnagar Petrol Rates (30th January 2024) - NDTV" />
        <meta property="og:description" content="Today's Bhavnagar Petrol Price is 97.77 rupee per litre: Here you can find Latest Petrol/Diesel Price in Bhavnagar city." />
         
        <meta property="og:image" content="https://www.ndtv.com/dstatic/images/Fuel-OG-English.png" />
                <meta name="twitter:title" content="Petrol Price in Bhavnagar Today | Check Bhavnagar Petrol Rates (30th January 2024) - NDTV" />
        <meta name="twitter:description" content="Today's Bhavnagar Petrol Price is 97.77 rupee per litre: Here you can find Latest Petrol/Diesel Price in Bhavnagar city." />
        <meta name="twitter:image" content="" />
                    <link rel="canonical" href="https://www.ndtv.com/fuel-prices/petrol-price-in-bhavnagar-city" />
                
        
                        <script type="application/ld+json">
     {"@context":"http:\/\/schema.org","@type":"WebPage","name":"Petrol Price in Bhavnagar Today | Check Bhavnagar Petrol Rates (30th January 2024) - NDTV","description":"Today's Bhavnagar Petrol Price is 97.77 rupee per litre: Here you can find Latest Petrol\/Diesel Price in Bhavnagar city.","publisher":{"@context":"http:\/\/schema.org","@type":"Organization","name":"NDTV","legalName":"NDTV","url":"https:\/\/www.ndtv.com","logo":"https:\/\/cdn.ndtv.com\/static\/ndtv_2014\/images\/ndtvlogo_blk.png"}}        
          </script>

          <script type="application/ld+json">
     {"@context":"http:\/\/schema.org","@type":"Organization","name":"NDTV","legalName":"NDTV","url":"https:\/\/www.ndtv.com","logo":"https:\/\/cdn.ndtv.com\/static\/ndtv_2014\/images\/ndtvlogo_blk.png"}        
          </script>

          
          
          
          <script>
               window.dataLayer = window.dataLayer || [];
               window.dataLayer.push({'SiteName': 'www.ndtv.com', 'PageType': 'home', "Platform": "desktop", 'language': 'english'});
               (function (w, d, s, l, i) {
                    w[l] = w[l] || [];
                    w[l].push({
                         'gtm.start': new Date().getTime(), event: 'gtm.js'
                    });
                    var f = d.getElementsByTagName(s)[0], j = d.createElement(s), dl = l != 'dataLayer' ? '&l=' + l : '';
                    j.async = true;
                    j.src = 'https://www.googletagmanager.com/gtm.js?id=' + i + dl;
                    f.parentNode.insertBefore(j, f);
               })(window, document, 'script', 'dataLayer', 'GTM-N2R2KQQ');
          </script>
          <!--End Google Tag Manager-->

          <!-- Begin comScore Tag -->
          <script>
               var _comscore = _comscore || [];
               _comscore.push({c1: "2", c2: "9548033"});
               (function () {
                    var s = document.createElement("script"), el = document.getElementsByTagName("script")[0];
                    s.async = true;
                    s.src = (document.location.protocol == "https:" ? "https://sb" : "http://b") + ".scorecardresearch.com/beacon.js";
                    el.parentNode.insertBefore(s, el);
               })();
          </script>
          <noscript>
     <img src="https://b.scorecardresearch.com/p?c1=2&c2=9548033&cv=2.0&cj=1" />
     </noscript>
     <link rel="icon" type="image/ico" href="https://www.ndtv.com/images/icons/ndtv.ico" />
          <!-- merge and include reset.css, helper.css, style.css, header.css and slide-nav.css -->
     <link href="https://www.ndtv.com/dstatic/css/atf.css?20230822-1" rel="stylesheet" />
     
               
          
     
               <link rel="manifest" href="https://www.ndtv.com/dstatic/manifest.json?v1">
     <style>
          .grecaptcha-badge{width: 1px !important;height: 1px !important;}
          table{margin:0 auto;}
          .menu {padding-bottom: 20px;}
          .menu a{padding:5px;}
          #pg_state{display:none;padding-top:50px;padding-bottom:50px;}
     </style>
     <script>
               var base_url = 'https://www.ndtv.com';
               var base_url = 'https://www.ndtv.com';
               var cdn_url = 'https://www.ndtv.com/dstatic';
               var shareURL = 'https://www.ndtv.com/fuel-prices/petrol-price-in-bhavnagar-city' || window.location.href;
     </script>
     <script>
          function chgSelect(fueltype, val, type) {
               if (val != 'select') {
                    var appstr='';
                                                  var dphref = 'https://www.ndtv.com/fuel-prices/' + fueltype + '-price-in-' + val + (type == 'state' ? '-state' : '-city');
                                   if(appstr)
                    dphref += (dphref.match(/\?/) ? '&' : '?') + appstr;
                    window.document.location.href=dphref;
               }
          }
     </script>
     <script src="https://www.ndtv.com/dstatic/js/lib.js?20220815-4"></script>
     <script src="https://cdn.ndtv.com/c/jquery-3.6.0.min.js"></script>
     <script type="text/javascript" >
               function setCookie(cname, cvalue, exdays, domain) {var d = new Date();d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));var domain = "domain=" + domain + ";"; if(domain == '') {domain = '';} var expires = "expires=" + d.toUTCString()+ ";"; if(exdays == '0') {expires = '';}document.cookie = cname + "=" + cvalue + "; " + expires + domain +" path=/";}
               function getCookie(cname) {var name = cname + "=";var ca = document.cookie.split(';');for (var i = 0; i < ca.length; i++) {var c = ca[i];while (c.charAt(0) == ' ')c = c.substring(1);if (c.indexOf(name) == 0)return c.substring(name.length, c.length);}return "";}
     </script>
     <!-- Ad Code for WAP -->
               <!-- Ad Code for Desktop -->
          
          <script type="text/javascript">
          var PWT = {};
          var googletag = googletag || {};
          googletag.cmd = googletag.cmd || [];
          var gptRan = false;
          PWT.jsLoaded = function () {
               loadGpt();
          };
          (function () {
               var purl = window.location.href;
               var url = '//ads.pubmatic.com/AdServer/js/pwt/158451/3766';
               var profileVersionId = '';
               if (purl.indexOf('pwtv=') > 0) {
                    var regexp = /pwtv=(.*?)(&|$)/g;
                    var matches = regexp.exec(purl);
                    if (matches.length >= 2 && matches[1].length > 0) {
                         profileVersionId = '/' + matches[1];
                    }
               }
               var wtads = document.createElement('script');
               wtads.async = true;
               wtads.type = 'text/javascript';
               wtads.src = url + profileVersionId + '/pwt.js';
               var node = document.getElementsByTagName('script')[0];
               node.parentNode.insertBefore(wtads, node);
          })();
          var loadGpt = function () {
               // Check the gptRan flag
               if (!gptRan) {
                    gptRan = true;
                    var gads = document.createElement('script');
                    var useSSL = 'https:' == document.location.protocol;
                    gads.src = (useSSL ? 'https:' : 'http:') + '//www.googletagservices.com/tag/js/gpt.js';
                    var node = document.getElementsByTagName('script')[0];
                    node.parentNode.insertBefore(gads, node);
               }
          }
          // Failsafe to call gpt
          setTimeout(loadGpt, 500);
     </script><!--Wrapper Script ends here --><script type="text/javascript">
          // this function will act as a lock and will call the GPT API
          function initAdserver(forced) {
               if ((forced === true && window.initAdserverFlag !== true) || (PWT.a9_BidsReceived && PWT.ow_BidsReceived)) {
                    window.initAdserverFlag = true;
                    PWT.a9_BidsReceived = PWT.ow_BidsReceived = false;
                    googletag.pubads().refresh();
               }
          }
     </script><script>
          !function (a9, a, p, s, t, A, g) { if (a[a9]) return; function q(c, r) { a[a9]._Q.push([c, r]) } a[a9] = { init: function () { q("i", arguments) }, fetchBids: function () { q("f", arguments) }, setDisplayBids: function () { }, targetingKeys: function () { return [] }, _Q: [] }; A = p.createElement(s); A.async = !0; A.src = t; g = p.getElementsByTagName(s)[0]; g.parentNode.insertBefore(A, g) }("apstag", window, document, "script", "//c.amazon-adsystem.com/aax2/apstag.js");
          apstag.init({
               pubID: '5d5467fe-bc8c-4335-993a-e0314547592e', //enter your pub ID here as shown above, it must within quotes
               adServer: 'googletag'
          });
          // APS request
          apstag.fetchBids({
                    slots: [{"slotID":"adslot728x90ATF","slotName":"\/1068322\/NDTV_News_Web_ROS_FuelPrices_728x90_ATF","sizes":[[728,90]]}],
               timeout: 1000 // Make Sure this timeout is less than or equal to OpenWrap TimeOut

          }, function (bids) {
               googletag.cmd.push(function () {
                    apstag.setDisplayBids();
                    PWT.a9_BidsReceived = true;
                    initAdserver(false);
               });
          });

     </script><!-- A9 Script End --><script type="text/javascript"> 
                    var utm_campaign = '';                
          
          googletag.cmd.push(function () {
               
                                   
          window.slot_1 = googletag.defineSlot('/1068322/NDTV_News_Web_ROS_FuelPrices_728x90_ATF', [[728, 90]], 'adslot728x90ATF').addService(googletag.pubads()).setTargeting('subsection','').setTargeting('storyid','').setTargeting('context','');    
                                        
                              googletag.pubads().enableLazyLoad({
                         fetchMarginPercent: 100, 
                         renderMarginPercent: 200,
                         });
                         googletag.enableServices();
                              googletag.pubads().enableSingleRequest();
                              googletag.pubads().disableInitialLoad();
     



          var trTagVal = getCookie('__ngutmtags'); 
          if(utm_campaign != '') {
          googletag.pubads().setTargeting('UTM', [utm_campaign]);
          } else if(trTagVal != '') {
          googletag.pubads().setTargeting('UTM', [trTagVal]);
          }
          var __gdpr = getCookie('__usrloc'); if(__gdpr == 'EU'){googletag.pubads().setRequestNonPersonalizedAds(1);}
     // OpenWrap code START here
               if (typeof PWT.requestBids === 'function') {
                    PWT.requestBids(
                         PWT.generateConfForGPT(googletag.pubads().getSlots()),
                         function (adUnitsArray) {
                         console.log("AdUnitsArray", adUnitsArray);
                         if (adUnitsArray[0].bidData.kvp.pwtplt == "video") {
                              var videoUrl = window.PWT.generateDFPURL(adUnitsArray[0], {
                                   section: 'blog',
                                   anotherKey: 'anotherValue'
                              });
                              invokeVideoPlayer(videoUrl);
                         } else {
                              PWT.addKeyValuePairsToGPTSlots(adUnitsArray);
                              PWT.ow_BidsReceived = true;
                              initAdserver(false);
                         }
                         });
               }
               // No need to handle "else" part as we have A9 wrapper on page
               // OpenWrap code END here
               var FAILSAFE_TIMEOUT = 1000; // this timeout should be more than OpenWrap and A9 timeout
               setTimeout(function () {
                    initAdserver(true); // calling this function with forced mode set to true so that GPT API is always executed
               }, FAILSAFE_TIMEOUT);
          });

          

     </script><script data-cfasync="false" type="text/javascript">
               (function (w, d) {
                    var s = d.createElement('script');
                    s.src = '//cdn.adpushup.com/42260/adpushup.js';
                    s.crossOrigin = 'anonymous';
                    s.type = 'text/javascript'; s.async = true;
                    (d.getElementsByTagName('head')[0] || d.getElementsByTagName('body')[0]).appendChild(s);
                    w.adpushup = w.adpushup || { que: [] };
               })(window, document);
               </script>
                         
          <script type="text/javascript">
          window._rrCode = window._rrCode || [];_rrCode.push(function(){
          window._taboola = window._taboola || [];
          !function (e, f, u) {
               e.async = 1;
               e.src = u;
               f.parentNode.insertBefore(e, f);
          }(document.createElement('script'), document.getElementsByTagName('script')[0], '//cdn.taboola.com/libtrc/ndtv-tools/loader.js');
          });
     </script>
     
          
     <script type="text/javascript">
     (function() {
          /** CONFIGURATION START **/
          var _sf_async_config = window._sf_async_config = (window._sf_async_config || {});
          _sf_async_config.uid = 34512;
          _sf_async_config.domain = 'fuel-price.ndtv.com';
          _sf_async_config.flickerControl = false;
          _sf_async_config.useCanonical = true;
          _sf_async_config.useCanonicalDomain = true;
          _sf_async_config.sections = ''; // CHANGE THIS TO YOUR SECTION NAME(s)
          _sf_async_config.authors = ''; // CHANGE THIS TO YOUR AUTHOR NAME(s)
          _sf_async_config.title = '';  // CHANGE THIS TO YOUR Headline
          _sf_async_config.type = '';  //CHANGE THIS AS PER PAGETYPE

          /** CONFIGURATION END **/
     function loadChartbeat() {
               var e = document.createElement('script');
               var n = document.getElementsByTagName('script')[0];
               e.type = 'text/javascript';
               e.async = true;
               e.src = '//static.chartbeat.com/js/chartbeat.js';;
               n.parentNode.insertBefore(e, n);
          }
          loadChartbeat();
          })();
     </script>
     <script async src="//static.chartbeat.com/js/chartbeat_mab.js"></script>
          <style>
          .container {
               max-width: 100%;
               margin: 0 auto;
          }

          .cent-wrp {
               max-width: 1080px;
               margin: 0 auto;
          }

          .sec_nv_cont {
               background-color: #f2f3f6;
               border-radius: 0 0 6px 6px;
               border-bottom: solid 1px #e7eaed;
          }


          .mid-cont {
               max-width: 820px;
               margin: 0 auto;
               padding: 0 10px;
          }

          div#adslot728x90ATF {
               text-align: center;
               display: flex;
               align-items: center;
               justify-content: center;
          }
     </style>
     
                                   <script>!function(a){var e="https://s.go-mpulse.net/boomerang/",t="addEventListener";if("False"=="True")a.BOOMR_config=a.BOOMR_config||{},a.BOOMR_config.PageParams=a.BOOMR_config.PageParams||{},a.BOOMR_config.PageParams.pci=!0,e="https://s2.go-mpulse.net/boomerang/";if(window.BOOMR_API_key="P4S98-FTZ59-DVK4T-C5SG5-AXGYM",function(){function n(e){a.BOOMR_onload=e&&e.timeStamp||(new Date).getTime()}if(!a.BOOMR||!a.BOOMR.version&&!a.BOOMR.snippetExecuted){a.BOOMR=a.BOOMR||{},a.BOOMR.snippetExecuted=!0;var i,_,o,r=document.createElement("iframe");if(a[t])a[t]("load",n,!1);else if(a.attachEvent)a.attachEvent("onload",n);r.src="javascript:void(0)",r.title="",r.role="presentation",(r.frameElement||r).style.cssText="width:0;height:0;border:0;display:none;",o=document.getElementsByTagName("script")[0],o.parentNode.insertBefore(r,o);try{_=r.contentWindow.document}catch(O){i=document.domain,r.src="javascript:var d=document.open();d.domain='"+i+"';void(0);",_=r.contentWindow.document}_.open()._l=function(){var a=this.createElement("script");if(i)this.domain=i;a.id="boomr-if-as",a.src=e+"P4S98-FTZ59-DVK4T-C5SG5-AXGYM",BOOMR_lstart=(new Date).getTime(),this.body.appendChild(a)},_.write("<bo"+'dy onload="document._l();">'),_.close()}}(),"".length>0)if(a&&"performance"in a&&a.performance&&"function"==typeof a.performance.setResourceTimingBufferSize)a.performance.setResourceTimingBufferSize();!function(){if(BOOMR=a.BOOMR||{},BOOMR.plugins=BOOMR.plugins||{},!BOOMR.plugins.AK){var e=""=="true"?1:0,t="",n="m4kb3oaxgl6vwznyoq2q-f-04719c722-clientnsv4-s.akamaihd.net",i="false"=="true"?2:1,_={"ak.v":"36","ak.cp":"349190","ak.ai":parseInt("216860",10),"ak.ol":"0","ak.cr":20,"ak.ipv":4,"ak.proto":"h2","ak.rid":"dcfdf48","ak.r":37487,"ak.a2":e,"ak.m":"dsca","ak.n":"essl","ak.bpcip":"103.20.29.0","ak.cport":63360,"ak.gh":"23.212.253.164","ak.quicv":"","ak.tlsv":"tls1.3","ak.0rtt":"","ak.csrc":"-","ak.acc":"","ak.t":"1706587189","ak.ak":"hOBiQwZUYzCg5VSAfCLimQ==qqK+0x2wYpOtt0mSPkhwVgaR0bfpklUjCFL8/vYHJoaFuGHhe/3FQQfOqRjmUz5JRdFcAggOmLFsqDOZAmPdkdt7A9rkzegnAY1LF92Vgte0KcBAUzkmkldX/loCe261xUdDdsPz2d4/St6GGFUhJsvFx5zvCzSgimR5JOQoRwMhacUqqi84eplDfC+hezpj6QdgR4Ruewzg7xNfL37DlFClCIdRx3hz2TbMmyAlf/sSqg8C2Tmt831IOX6qqpToeixGYY6jWoG+ZdKxUZFQnSnNNow2BrjYurmKqkzY8CMoHs04nDMp/q7r4YrDmTBIWzPEuY9UlsSyI2qgjtkHTaos+DpdC4O+iqG9PXVVYDbZcW2DUR+E6ckJwQoZDk2q1yhqMN8aRbTtitXjb+zPkHietLXH6pydogP5KBTpDUc=","ak.pv":"125","ak.dpoabenc":"","ak.tf":i};if(""!==t)_["ak.ruds"]=t;var o={i:!1,av:function(e){var t="http.initiator";if(e&&(!e[t]||"spa_hard"===e[t]))_["ak.feo"]=void 0!==a.aFeoApplied?1:0,BOOMR.addVar(_)},rv:function(){var a=["ak.bpcip","ak.cport","ak.cr","ak.csrc","ak.gh","ak.ipv","ak.m","ak.n","ak.ol","ak.proto","ak.quicv","ak.tlsv","ak.0rtt","ak.r","ak.acc","ak.t","ak.tf"];BOOMR.removeVar(a)}};BOOMR.plugins.AK={akVars:_,akDNSPreFetchDomain:n,init:function(){if(!o.i){var a=BOOMR.subscribe;a("before_beacon",o.av,null,null),a("onbeacon",o.rv,null,null),o.i=!0}return this},is_complete:function(){return!0}}}}()}(window);</script></head>
     <body>
     
     <!-- Google Tag Manager (noscript) -->
     <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-N2R2KQQ" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
     <!-- End Google Tag Manager (noscript) -->
     <div class="container">
          <header class="global-header">
               <div class="cent-wrp">
                    <div class="gh-inner">

                         <a href="javascript:void(0)" class="gh-burg">
                         <svg class="burg-icn" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                              <path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"></path>
                         </svg>
                         </a>
                    <div class="gh-logo">
                              <a class="gh-logo_anch" href="https://www.ndtv.com/tools">
                              <span class="gh-logo_svg">
                              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 241.47 20.8">
     <path class="ndtv-lg" d="m108.94,5.27v7.49c.06,1.11-.37,2.18-1.17,2.95-.88.76-2.03,1.15-3.19,1.09-1.15.06-2.28-.32-3.17-1.06-.8-.75-1.24-1.8-1.2-2.9v-7.58h2.35v7.51c-.05.59.14,1.18.53,1.63.41.36.94.54,1.48.51,1.32,0,1.99-.69,2.01-2.08v-7.57h2.35Zm3.74,9.49h4.98v1.88h-7.32V5.27h2.34v9.49Zm12.75-7.59h-3.48v9.48h-2.34V7.16h-3.44v-1.9h9.27v1.9Zm3.3,9.48h-2.34V5.27h2.34v11.38Zm4.71-11.38l2.92,8.25,2.91-8.25h3.08v11.38h-2.35v-3.11l.23-5.37-3.07,8.48h-1.61l-3.06-8.47.23,5.36v3.11h-2.34V5.27h3.06Zm16.99,9.03h-4.11l-.78,2.34h-2.49l4.23-11.38h2.17l4.26,11.38h-2.49l-.79-2.34Zm-3.48-1.9h2.84l-1.43-4.26-1.41,4.26Zm14.92-5.23h-3.49v9.48h-2.34V7.16h-3.44v-1.9h9.27v1.9Zm7.65,4.55h-4.5v3.05h5.28v1.88h-7.62V5.27h7.61v1.9h-5.27v2.71h4.5v1.83Zm13.18-4.55h-3.48v9.48h-2.35V7.16h-3.44v-1.9h9.27v1.9Zm9.93,4.05c.02,1.01-.18,2.02-.59,2.94-.36.8-.95,1.48-1.7,1.95-.76.47-1.64.7-2.54.69-.89.01-1.76-.22-2.52-.68-.75-.47-1.35-1.14-1.72-1.94-.42-.91-.63-1.9-.62-2.9v-.56c-.02-1.02.19-2.03.6-2.96.37-.81.96-1.49,1.71-1.96.76-.46,1.64-.7,2.53-.68.89-.02,1.77.22,2.53.68.75.47,1.35,1.15,1.71,1.96.42.93.63,1.93.61,2.95v.51Zm-2.38-.52c.06-.95-.16-1.9-.64-2.72-.4-.61-1.1-.96-1.83-.93-.72-.03-1.41.32-1.82.92-.48.81-.71,1.75-.65,2.69v.56c-.05.94.17,1.88.64,2.7.4.63,1.1.99,1.84.96.73.03,1.41-.32,1.82-.92.47-.82.7-1.76.64-2.7v-.56Zm12.89.52c.02,1.01-.18,2.02-.59,2.94-.36.8-.95,1.48-1.7,1.95-.76.47-1.64.71-2.54.69-.89.01-1.76-.22-2.52-.68-.75-.47-1.35-1.14-1.72-1.94-.42-.91-.63-1.9-.62-2.9v-.56c-.02-1.02.19-2.03.6-2.96.37-.81.96-1.49,1.71-1.96.76-.46,1.64-.7,2.53-.68.89-.02,1.77.22,2.53.68.75.47,1.35,1.15,1.71,1.96.42.93.63,1.93.61,2.95v.51Zm-2.37-.52c.06-.95-.16-1.9-.64-2.72-.4-.61-1.1-.96-1.83-.93-.72-.03-1.41.32-1.82.92-.48.81-.71,1.75-.65,2.69v.56c-.05.94.17,1.88.64,2.7.4.63,1.1.99,1.84.97.72.03,1.41-.32,1.81-.93.47-.82.7-1.76.64-2.7v-.55Zm5.9,4.06h4.98v1.88h-7.32V5.27h2.34v9.49Zm5.79,1.88V5.27h3.98c1.1-.07,2.2.2,3.14.79.72.55,1.12,1.42,1.07,2.32.01.52-.14,1.04-.43,1.47-.29.43-.71.76-1.2.93.55.12,1.04.44,1.38.88.34.47.52,1.04.5,1.62.07.95-.32,1.87-1.04,2.48-.87.62-1.92.92-2.98.86h-4.42Zm2.34-4.95v3.07h2.01c.46.03.92-.11,1.29-.4.31-.27.49-.67.47-1.09.05-.44-.1-.88-.42-1.19-.32-.31-.76-.46-1.2-.39h-2.15Zm0-1.66h1.73c1.19-.02,1.78-.49,1.78-1.41.04-.42-.13-.84-.45-1.11-.43-.26-.92-.38-1.42-.34h-1.64v2.87Zm16.68,1.18c.02,1.01-.18,2.02-.59,2.94-.36.8-.95,1.48-1.7,1.95-.76.47-1.64.7-2.53.69-.89.01-1.76-.22-2.52-.68-.75-.47-1.35-1.14-1.72-1.94-.42-.91-.63-1.9-.62-2.9v-.56c-.02-1.02.19-2.03.6-2.96.37-.81.96-1.49,1.71-1.96.76-.46,1.64-.7,2.53-.68.89-.02,1.77.22,2.53.68.75.47,1.35,1.15,1.71,1.96.42.93.63,1.93.6,2.95v.51Zm-2.37-.52c.06-.95-.16-1.9-.64-2.72-.4-.61-1.1-.96-1.83-.93-.72-.03-1.41.32-1.82.92-.48.81-.71,1.75-.65,2.69v.56c-.05.94.17,1.88.64,2.7.4.63,1.1.99,1.84.96.73.03,1.41-.32,1.81-.93.47-.82.7-1.76.64-2.7v-.55Zm7.45-1.51l2.13-3.92h2.7l-3.32,5.64,3.4,5.73h-2.73l-2.19-3.98-2.19,3.98h-2.73l3.4-5.73-3.31-5.64h2.7l2.13,3.92ZM12.8,13.69c-.85,0-1.37-.87-1.58-1.27l-2.17-4.49c-.85-1.98-2.76-3.28-4.91-3.36H0v12.77h4.01v-9.11h.13c.9,0,1.45.96,1.58,1.27l2.22,4.49c.8,1.99,2.71,3.32,4.86,3.36h4.1V4.58h-3.97v9.11h-.13Zm31.34,3.66h-3.82V7.59h-5.95c.21.81.31,1.64.3,2.48v1.39c.1,1.56-.38,3.1-1.36,4.31-1.09,1.1-2.61,1.68-4.16,1.57h-10.84V4.58h33.78l5.14,9.5,4.84-9.5h4.12l-6.58,12.77h-4.8l-5.31-9.76h-5.35v9.76h0Zm-17.63-3.01h2.08c1.49,0,2.21-.66,2.21-2.01v-2.79c0-1.24-.8-1.96-2.21-1.96h-6.41v6.75h4.33ZM89.84,0l.63.81-.92,1.58.95.55.9-1.58,1.02.14.68,2.55c.2.79-.26,1.59-1.04,1.81l-2.04.55-5.31,9.19-.06.1.05.11c.66,1.38.34,3.03-.78,4.06-1.12,1.04-2.79,1.22-4.11.45-1.32-.77-1.99-2.31-1.64-3.8.34-1.49,1.62-2.58,3.14-2.69h.11s5.32-9.22,5.32-9.22l.05-.08-.54-2.05c-.2-.79.26-1.59,1.04-1.82l2.55-.68Zm-.64,10.76l3.2,5.55c.81,1.42.34,3.24-1.07,4.07l-.07.04c-.44.25-.94.38-1.44.38h-.22c-1-.07-1.9-.63-2.39-1.5l-1.35-2.34.81-.46,1.34,2.34c.42.73,1.24,1.13,2.07,1.01l.33-.05-3.48-6.04.81-.47,3.48,6.04.21-.26c.51-.66.57-1.57.16-2.29l-3.19-5.55.81-.47Zm0-9.61l-1.66.44c-.29.08-.46.38-.38.67l.64,2.4-5.83,10.12h-.49c-1.41.01-2.53,1.18-2.5,2.58.02,1.41,1.19,2.53,2.6,2.51h0c.93,0,1.78-.51,2.23-1.32.45-.81.42-1.8-.08-2.59l-.15-.24,5.84-10.11,2.4-.64c.29-.08.46-.37.39-.67l-.44-1.66-.92,1.59-2.57-1.49.92-1.58Zm-7.66,14.38c.35,0,.69.1.98.3l.09.06-.54.77-.02-.02c-.17-.14-.38-.2-.6-.18-.22.02-.42.13-.56.3-.28.36-.23.87.12,1.16.02.02.05.03.07.05l.04.03-.53.77-.04-.02c-.39-.26-.65-.67-.74-1.12s0-.93.27-1.32c.26-.39.66-.66,1.12-.75.11-.02.23-.03.34-.03Zm-2.51-9.88v.94h-4.78c-.46,0-.83.37-.83.82v2.97h8.19v.94h-7.32s0,5.13,0,5.13c0,.22.09.43.24.58.15.15.36.24.58.24h1.79v.94h-1.79c-.97,0-1.76-.79-1.76-1.76v-5.13h-.86v-3.91c0-.97.79-1.76,1.76-1.76h4.78Zm1.84-5.5l2.08.55,1.64,2.85-.42,1.54.58,1-.81.46-.79-1.32.42-1.54-1.26-2.17-1.32-.36-1.2.69-.35,1.33,1.25,2.17,1.55.41,1.35,2.33-.81.47-1.16-2-1.54-.41-1.65-2.85.55-2.08,1.88-1.08Z"></path>
     <path fill="#d82a2d" d="m17.93,13.8c-1.35,0-2.44-1.11-2.44-2.46,0-1.36,1.08-2.47,2.44-2.51,1.38,0,2.49,1.13,2.49,2.51,0,.66-.27,1.29-.73,1.75s-1.1.72-1.76.71Z"></path>
     </svg>
                              </span> 

                                   <span class="link-title">NDTV Ultimate Toolbox</span>

                                   </a>
                         </div>
                         
                         <div class="hdrIcns d-flex">
                         <span class="shareIcn pos-rel is-hidden" onclick="nativeShare();"></span>
                         </div>
                         <div id="___ndtvspldiv"></div>

                    </div>

                    
                              </div>

          </header>
          
                    
          
               
          
               
          
          <div class="socialShr">
               <ul>
                    <li><a href="javascript:void(0)" onClick="shreNow('fb');" class="fbicn"></a></li>
                    <li><a href="javascript:void(0)" onClick="shreNow('tw');" class="twicn"></a></li>
                    <li><a href="javascript:void(0)" onClick="shreNow('wa');" class="whicn"></a></li>
                    <li><a href="javascript:void(0)" onClick="shreNow('rd');" class="reicn"></a></li>
                    <li><a href="javascript:void(0)" onClick="shreNow('ln');" class="lnicn"></a></li>
                    <li><a href="javascript:void(0)" onClick="shreNow('mail');" class="mlicn"></a></li>
                    <li><a href="javascript:void(0)" onClick="shreNow('sms');" class="chicn"></a></li>
                    <li><a href="javascript:void(0)" onClick="shreNow('snapchat');" class="snicn"></a></li>
               </ul>
          </div>
                    <script>
               function shreNow(type, text, pageType='', siteName='') {
                    if(pageType==''){
                         var pageType='fuel-price';
                    }
                    if(siteName==''){
                         var siteName='NDTV fuel-price';
                    }
                    if("" == 'IFSC'){
                         if (type == 'fb') {
                         var url = shareURL;
                         }else{
                         var url = "Get bank IFSC codes at your fingertips with "+shareURL;
                         }
                    } else if("" == 'PINCODES'){
                         if (type == 'fb') {
                         var url = shareURL;
                         }else{
                         var url = "Get PIN code and post-office-related info at your fingertips with "+shareURL;
                         }
                    }
                    else{
                         var url = shareURL;
                    }
                    
                    var srl = '';
                    if (type == 'fb') {
                         srl = 'https://www.facebook.com/sharer/sharer.php?u=' + url;
                    } else if (type == 'tw') {
                         srl = 'https://twitter.com/intent/tweet?url=' + url;
                    } else if (type == 'wa') {
                         srl = 'https://api.whatsapp.com//send?text=' + url;
                    } else if (type == 'mail') {
                         srl = 'mailto:?subject=' + url + '&body=' + url;
                    } else if (type == 'ln') {
                         srl = 'https://www.linkedin.com/cws/share?url=' + url;
                    } else if (type == 'rd') {
                         srl = 'https://reddit.com/submit?url=' + url;
                    } else if (type == 'sms') {
                         srl = 'sms:?text=' + url;
                    } else if (type == 'snapchat') {
                         srl = 'https://www.snapchat.com/scan?attachmentUrl=' + url;
                    }

                    dataLayer.push({'event':'social_icon_top',
                         'eventCategory':'social icon top',
                         'eventAction':'top icon clicked',
                         'eventLabel':type,
                         'PageType':pageType,
                         'SiteName':siteName,
                         'URL':url,
                         'Article Category':''
                    });

                    window.open(srl, '_blank', 'location=yes,height=500,width=500,scrollbars=yes,status=yes');
               }

               if (navigator.share) {
                    var tmp = document.querySelector('.shareIcn');
                    if (tmp) {
                         tmp.style.display = 'block';
                         document.querySelector('.socialShr').style.display = 'none';
                    }
               }

               function nativeShare() {
                    navigator.share({
                         title: 'NDTV',
                         url: shareURL
                    }).then(() => {
                         //console.log('Thanks for sharing!');
                    }).catch(
                         //console.error
                         );
               }
          </script>
               <div class="mid-cont">
               <span class="ptb-12 font-13 brdCrumb">
          <a href="https://www.ndtv.com/tools">Home</a>
          
                                   <a href='https://www.ndtv.com/fuel-prices'>Fuel Price</a>                                    <a href='https://www.ndtv.com/fuel-prices/petrol-price-in-gujarat-state'>Gujarat</a>                                    <span>Petrol Price In Bhavnagar</span>                </span>
     <!-- =======[Ad Position]======= -->
          <div class="ad_placeholder mb-20">
               
               <div class="adtext">Advertisement</div> 
               
                              <div class="ad_place-wrap dsk-ad">
                              <div id='adslot728x90ATF' style='min-width: 728px; min-height: 90px;'>
                              <script>
                              googletag.cmd.push(function() { googletag.display('adslot728x90ATF'); });    
                              </script>
                              </div>
                         
                    </div>
                         
          </div>
          

     <script type="application/ld+json">
     {"@context":"https:\/\/schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"item":{"@id":"https:\/\/www.ndtv.com\/fuel-prices","name":"Fuel Price"}},{"@type":"ListItem","position":2,"item":{"@id":"https:\/\/www.ndtv.com\/fuel-prices\/petrol-price-in-gujarat-state","name":"Gujarat"}},{"@type":"ListItem","position":3,"item":{"@id":"https:\/\/www.ndtv.com","name":"Petrol Price In Bhavnagar"}}]}</script>        <link href="https://www.ndtv.com/dstatic/css/select2.min.css?20230822-1" rel="stylesheet" />
     <script  src="https://www.ndtv.com/dstatic/js/select2.min.js?20220815-4"></script>
     <main class="p-20 pt-0">
     <section class="fullIcnbr withIcn mb-16 mt-20 t-center ptrolIcn">
          <div class="usrDta active">
                                   <h1 class="hdngStyle2">Petrol Price in Bhavnagar</h1>
                              </div>
     </section>
     <section class="pg_copy pb-15">
          <p class="color-blue lh-1-7 t-center mt-20 mb-20">
                                                            Petrol price today in Bhavnagar (Gujarat) is Rs. 97.77 per litre.
                                             The last change in Bhavnagar's petrol price was on Jan 29, 2024                         and it was decreased by -0.77 rupees.                       
                                                                      In the last 10 days, the petrol price in Bhavnagar has been fluctuating between Rs 97.67 and Rs 98.54.
                    
                    You can also check petrol rate in other areas of Gujarat today and the change in the pricing in comparison to the previous day. The petrol price is inclusive of Gujarat state taxes.
                    <?php}?>
                    
                                             </p>
     </section>
          <!-- comment <h2 class="hdngStyle2">Today's Petrol Price in Bhavnagar is 97.77 rs/L</h2>-->
     <section class="todyPricContnr mb-16 bg_blue1 b_rad4 w-100 d-flex pos-rel">
          
          <div class="prcContnr pl-10 mt-5">
               
               <h4 class="font-15 color-blue mb-5">Jan 30, 2024 Price</h4>
               <span class="font-b color-blue">97.77 <span class="font-16">₹/L</span></span>
          </div>
          <div class="btnContnr" style="display:none;">
               <a href="javascript:void(0)" onclick="notiClick('p_city-81');" class="icnBx font-b notfcn t-h-no-decor d-flex btnStyl3 pos-rel">
                    <span class="pos-rel  d-flex jc-center ai-center font-14">Get Notificaiton
                         for Bhavnagar's Petrol Price</span>
               </a>
          </div>
     </section>
               <section class="pt_ds_prc mt-15 bg_blue1 p-15 b_rad4">
     <div class="tp_br d-flex ai-center mb-16">
          <div class="city_selct d-flex mr-auto pos-rel">
               <span class="is-block selctDsgn selctMenu_n d-flex ai-center">
                    <select id="sdropdown" onchange="chgSelect('petrol',this.options[this.selectedIndex].value, 'state');">
                         <option value="select">Select State</option>
                                             <option value="andaman-and-nicobar" >Andaman And Nicobar</option>
                                             <option value="andhra-pradesh" >Andhra Pradesh</option>
                                             <option value="arunachal-pradesh" >Arunachal Pradesh</option>
                                             <option value="assam" >Assam</option>
                                             <option value="bihar" >Bihar</option>
                                             <option value="chandigarh" >Chandigarh</option>
                                             <option value="chhattisgarh" >Chhattisgarh</option>
                                             <option value="dadra-and-nagar-haveli" >Dadra And Nagar Haveli</option>
                                             <option value="daman-and-diu" >Daman And Diu</option>
                                             <option value="delhi" >Delhi</option>
                                             <option value="goa" >Goa</option>
                                             <option value="gujarat" selected>Gujarat</option>
                                             <option value="haryana" >Haryana</option>
                                             <option value="himachal-pradesh" >Himachal Pradesh</option>
                                             <option value="jammu-and-kashmir" >Jammu And Kashmir</option>
                                             <option value="jharkhand" >Jharkhand</option>
                                             <option value="karnataka" >Karnataka</option>
                                             <option value="kerala" >Kerala</option>
                                             <option value="madhya-pradesh" >Madhya Pradesh</option>
                                             <option value="maharashtra" >Maharashtra</option>
                                             <option value="manipur" >Manipur</option>
                                             <option value="meghalaya" >Meghalaya</option>
                                             <option value="mizoram" >Mizoram</option>
                                             <option value="nagaland" >Nagaland</option>
                                             <option value="odisha" >Odisha</option>
                                             <option value="puducherry" >Puducherry</option>
                                             <option value="punjab" >Punjab</option>
                                             <option value="rajasthan" >Rajasthan</option>
                                             <option value="sikkim" >Sikkim</option>
                                             <option value="tamil-nadu" >Tamil Nadu</option>
                                             <option value="telangana" >Telangana</option>
                                             <option value="tripura" >Tripura</option>
                                             <option value="uttar-pradesh" >Uttar Pradesh</option>
                                             <option value="uttarakhand" >Uttarakhand</option>
                                             <option value="west-bengal" >West Bengal</option>
                                        </select>
               </span>
               <span class="is-block selctDsgn selctMenu_n d-flex ai-center">
                    <select id="cdropdown" onchange="chgSelect('petrol',this.options[this.selectedIndex].value, 'city');">
                         <option value="select">Select City/District</option>
                                             <option value="ahmedabad" >Ahmedabad</option>
                                             <option value="amreli" >Amreli</option>
                                             <option value="anand" >Anand</option>
                                             <option value="aravalli" >Aravalli</option>
                                             <option value="banas-kantha" >Banas Kantha</option>
                                             <option value="bharuch" >Bharuch</option>
                                             <option value="bhavnagar" selected>Bhavnagar</option>
                                             <option value="botad" >Botad</option>
                                             <option value="chhotaudepur" >Chhotaudepur</option>
                                             <option value="dahod" >Dahod</option>
                                             <option value="devbhumi-dwarka" >Devbhumi Dwarka</option>
                                             <option value="gandhi-nagar" >Gandhi Nagar</option>
                                             <option value="gir-somnath" >Gir Somnath</option>
                                             <option value="jamnagar" >Jamnagar</option>
                                             <option value="junagadh" >Junagadh</option>
                                             <option value="kheda" >Kheda</option>
                                             <option value="kutch" >Kutch</option>
                                             <option value="mahisagar" >Mahisagar</option>
                                             <option value="mehsana" >Mehsana</option>
                                             <option value="morbi" >Morbi</option>
                                             <option value="narmada" >Narmada</option>
                                             <option value="navsari" >Navsari</option>
                                             <option value="panch-mahal" >Panch Mahal</option>
                                             <option value="patan" >Patan</option>
                                             <option value="porbander" >Porbander</option>
                                             <option value="rajkot" >Rajkot</option>
                                             <option value="sabar-kantha" >Sabar Kantha</option>
                                             <option value="surat" >Surat</option>
                                             <option value="surendranagar" >Surendranagar</option>
                                             <option value="tapi" >Tapi</option>
                                             <option value="the-dangs" >The Dangs</option>
                                             <option value="vadodara" >Vadodara</option>
                                             <option value="valsad" >Valsad</option>
                                        </select>
               </span>
               </div>
          <span class="dt_blk font-12 ml-10 mr-auto">Updated:Jan 30, 2024</span>

     </div> 
     </section>
          <section class="pt_ds_prc bg_blue1 p-15 b_rad10 mt-10">
                         <h3 class="font-18 color-blue font-500 t-center mb-16">Last 10 Days Petrol Prices In Bhavnagar</h3>
                    <div class="tabs_cont">
                         <div class="tb-data-outer p-15 b_rad4 bg-wht pos-rel">
                         <div class="tb-data-con">

                              <div class="tbl-container b_rad4 overflow-hidden">
                                   <table width="100%" class="font-16 color-blue" border="0" cellspacing="0" cellpadding="0">
                                        <tbody><tr class="bg_blue1">
                         <th scope="col">Date</th>
                         <th scope="col"> Price</th>
                         <th scope="col">Change</th>
                         </tr><tr><td>Jan 30, 2024</a></td>
                         <td>97.77 ₹/L</td>
                         <td><span class="chngBx up">0.77</span></td></tr><tr><td>Jan 29, 2024</a></td>
                         <td>98.54 ₹/L</td>
                         <td><span class="chngBx down">0.44</span></td></tr><tr><td>Jan 28, 2024</a></td>
                         <td>98.10 ₹/L</td>
                         <td><span class="chngBx up">0.38</span></td></tr><tr><td>Jan 27, 2024</a></td>
                         <td>98.48 ₹/L</td>
                         <td><span class="chngBx down">0.71</span></td></tr><tr><td>Jan 26, 2024</a></td>
                         <td>97.77 ₹/L</td>
                         <td><span class="chngBx up">0.33</span></td></tr><tr><td>Jan 25, 2024</a></td>
                         <td>98.10 ₹/L</td>
                         <td><span class="chngBx down">0.11</span></td></tr><tr><td>Jan 24, 2024</a></td>
                         <td>97.99 ₹/L</td>
                         <td><span class="chngBx up">0.11</span></td></tr><tr><td>Jan 23, 2024</a></td>
                         <td>98.10 ₹/L</td>
                         <td><span class="chngBx up">0.15</span></td></tr><tr><td>Jan 22, 2024</a></td>
                         <td>98.25 ₹/L</td>
                         <td><span class="chngBx down">0.58</span></td></tr><tr><td>Jan 21, 2024</a></td>
                         <td>97.67 ₹/L</td>
                         <td><span class="chngBx up">0.81</span></td></tr></tbody>
                                   </table>
                              </div>
                         </div>
                         </div>
                    </div>
                                             <div class="tabs_cont  mt-20">
               <h3 class="font-18 color-blue font-500 t-center mb-16">
                                                       Petrol Price In Other Cities And Districts Of Gujarat                                               </h3>
               <div class="tb-bar">
                    <ul class="d-flex jc-center">
                         <li class="active">
                         <a class="is-block" id="myIDD1" href="https://www.ndtv.com/fuel-prices/petrol-price-in-bhavnagar-city">Petrol</a>
                         </li>
                         <li >
                         <a class="is-block" id="myIDD2" href="https://www.ndtv.com/fuel-prices/diesel-price-in-bhavnagar-city">Diesel</a>
                         </li>
                    </ul>
               </div>
                    <link href="https://www.ndtv.com/dstatic/css/jquery-ui.css?20230822-1" rel="stylesheet" />
     <script  src="https://www.ndtv.com/dstatic/js/jquery-ui.min.js?20220815-4"></script>
     <div id="myID" class="tb-data-outer p-15 b_rad4 bg-wht pos-rel">
     <div class="tb-data-con"><div class="tbl-container b_rad4">
               <table width="100%" class="font-16 color-blue short-nm" border="0" cellspacing="0" cellpadding="0">
                    <tbody><tr class="bg_blue1">
                         <th scope="col">City/District</th>
                         <th scope="col">Price</th>
                         <th scope="col">Change</th>
                         </tr><tr><td id="A"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-ahmedabad-city">Ahmedabad</a></td>
                         <td>96.98 ₹/L</td>
                         <td><span class="chngBx down">0.58</span></td></tr><tr><td id="A"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-amreli-city">Amreli</a></td>
                         <td>97.95 ₹/L</td>
                         <td><span class="chngBx down">0.33</span></td></tr><tr><td id="A"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-anand-city">Anand</a></td>
                         <td>96.59 ₹/L</td>
                         <td><span class="chngBx down">0.13</span></td></tr><tr><td id="A"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-aravalli-city">Aravalli</a></td>
                         <td>97.16 ₹/L</td>
                         <td><span class="chngBx up">0.10</span></td></tr><tr><td id="B"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-banas-kantha-city">Banas Kantha</a></td>
                         <td>96.62 ₹/L</td>
                         <td><span class="chngBx up">0.53</span></td></tr><tr><td id="B"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-bharuch-city">Bharuch</a></td>
                         <td>96.99 ₹/L</td>
                         <td><span class="chngBx down">0.14</span></td></tr><tr><td id="B"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-bhavnagar-city">Bhavnagar</a></td>
                         <td>97.77 ₹/L</td>
                         <td><span class="chngBx up">0.77</span></td></tr><tr><td id="B"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-botad-city">Botad</a></td>
                         <td>97.69 ₹/L</td>
                         <td><span class="chngBx down">0.26</span></td></tr><tr><td id="C"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-chhotaudepur-city">Chhotaudepur</a></td>
                         <td>96.41 ₹/L</td>
                         <td><span class="chngBx up">0.33</span></td></tr><tr><td id="D"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-dahod-city">Dahod</a></td>
                         <td>96.96 ₹/L</td>
                         <td><span class="chngBx up">0.13</span></td></tr><tr><td id="D"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-devbhumi-dwarka-city">Devbhumi Dwarka</a></td>
                         <td>96.77 ₹/L</td>
                         <td><span class="chngBx down">0.56</span></td></tr><tr><td id="G"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-gandhi-nagar-city">Gandhi Nagar</a></td>
                         <td>96.64 ₹/L</td>
                         <td><span class="chngBx up">0.23</span></td></tr><tr><td id="G"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-gir-somnath-city">Gir Somnath</a></td>
                         <td>97.82 ₹/L</td>
                         <td><span class="chngBx up">0.46</span></td></tr><tr><td id="J"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-jamnagar-city">Jamnagar</a></td>
                         <td>96.04 ₹/L</td>
                         <td><span class="chngBx up">0.39</span></td></tr><tr><td id="J"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-junagadh-city">Junagadh</a></td>
                         <td>97.73 ₹/L</td>
                         <td><span class="chngBx down">0.33</span></td></tr><tr><td id="K"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-kheda-city">Kheda</a></td>
                         <td>96.43 ₹/L</td>
                         <td><span class="chngBx up">0.22</span></td></tr><tr><td id="K"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-kutch-city">Kutch</a></td>
                         <td>96.81 ₹/L</td>
                         <td><span class="chngBx up">0.67</span></td></tr><tr><td id="M"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-mahisagar-city">Mahisagar</a></td>
                         <td>97.16 ₹/L</td>
                         <td><span class="chngBx down">0.09</span></td></tr><tr><td id="M"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-mehsana-city">Mehsana</a></td>
                         <td>96.40 ₹/L</td>
                         <td><span class="chngBx up">0.21</span></td></tr><tr><td id="M"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-morbi-city">Morbi</a></td>
                         <td>96.77 ₹/L</td>
                         <td><span class="chngBx down">0.45</span></td></tr><tr><td id="N"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-narmada-city">Narmada</a></td>
                         <td>96.99 ₹/L</td>
                         <td><span class="chngBx down">0.27</span></td></tr><tr><td id="N"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-navsari-city">Navsari</a></td>
                         <td>96.54 ₹/L</td>
                         <td><span class="chngBx up">0.58</span></td></tr><tr><td id="P"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-panch-mahal-city">Panch Mahal</a></td>
                         <td>96.44 ₹/L</td>
                         <td><span class="chngBx up">0.32</span></td></tr><tr><td id="P"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-patan-city">Patan</a></td>
                         <td>96.22 ₹/L</td>
                         <td><span class="chngBx up">0.46</span></td></tr><tr><td id="P"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-porbander-city">Porbander</a></td>
                         <td>96.85 ₹/L</td>
                         <td><span class="chngBx up">1.11</span></td></tr><tr><td id="R"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-rajkot-city">Rajkot</a></td>
                         <td>96.19 ₹/L</td>
                         <td><span class="chngBx up">0.33</span></td></tr><tr><td id="S"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-sabar-kantha-city">Sabar Kantha</a></td>
                         <td>97.32 ₹/L</td>
                         <td><span class="chngBx up">0.37</span></td></tr><tr><td id="S"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-surat-city">Surat</a></td>
                         <td>96.51 ₹/L</td>
                         <td><span class="chngBx down">0.21</span></td></tr><tr><td id="S"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-surendranagar-city">Surendranagar</a></td>
                         <td>97.15 ₹/L</td>
                         <td><span class="chngBx up">0.06</span></td></tr><tr><td id="T"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-tapi-city">Tapi</a></td>
                         <td>96.99 ₹/L</td>
                         <td><span class="chngBx down">0.11</span></td></tr><tr><td id="T"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-the-dangs-city">The Dangs</a></td>
                         <td>97.25 ₹/L</td>
                         <td><span class="chngBx up lr">0.00</span></td></tr><tr><td id="V"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-vadodara-city">Vadodara</a></td>
                         <td>96.08 ₹/L</td>
                         <td><span class="chngBx down">0.02</span></td></tr><tr><td id="V"><a href="https://www.ndtv.com/fuel-prices/petrol-price-in-valsad-city">Valsad</a></td>
                         <td>97.39 ₹/L</td>
                         <td><span class="chngBx down">0.11</span></td></tr></tbody>
               </table></div>
     </div>
     </div><div class="search_item"></div>
     <script>
          var fuelType= 'patrol';
          var fuelLoc= 'city';
          var categoryPageLimit = 125;
          function loadCategory() { //alert(fuelType);
               var params = "page/" + fuelType + '/pagelimit/'+categoryPageLimit;
               var ajaxURL = "https://www.ndtv.com/fuel-prices/getLoadMoreDataDetails/" + params;
               //alert(ajaxURL);
               categoryPageLimit = categoryPageLimit+100;
               $.ajax({     
                         type: "GET",
                         url: ajaxURL,
                         success: function (data) { console.log(data);
                              $('#myID').hide();
                              $('.search_item').html(''); 
                              $('.search_item').html(data); 
                         },
                         error: function (data) {
                         console.log('Error');   
                         },
                         });
          }
          
          function search_city() {
               var search_val = $('#autocomplete').val();
               //alert(search_val);//exit;
               var params = "page/" + fuelType + '/key/'+search_val;
               var lang = 'en';
               if(lang==='hi'){
               var ajaxURL = "https://www.ndtv.com/tools/fuel-rate/getSearchListDetails/" + params;
               }else{
               var ajaxURL = "https://www.ndtv.com/fuel-prices/getSearchListDetails/" + params;    
               }
               $.ajax({     
                         type: "GET",
                         url: ajaxURL,
                         success: function (data) { console.log(data);
                              $('#myID').hide();
                              $('.search_item').html(''); 
                              $('.search_item').html(data); 
                         },
                         error: function (data) {
                         console.log('Error');   
                         },
                         });
          }
          
     </script>
     <script type='text/javascript' >
     $( function() {
     
          $( "#autocomplete" ).autocomplete({
               source: function( request, response ) {
                    var search = request.term;
                    var params = "page/" + search;
                    var lang = 'en';
                    if(lang==='hi'){
                    var ajaxURL = "https://www.ndtv.com/tools/fuel-rate/getCity/" + params;
                    }else{
                    var ajaxURL = "https://www.ndtv.com/fuel-prices/getCity/" + params;    
                    }
                    //alert(ajaxURL);
                    $.ajax({
                         url: ajaxURL,
                         type: "GET",
                         dataType: "json",
                    // data: {
                         //   search: request.term
                    // },
                         success: function( data ) {
                         console.log(data);
                         response( data );
                         }
                         
                    });
               },
                         select: function (event, ui) {
                         $('#autocomplete').val(ui.item.label); // display the selected text
                         search_city();
                         return false;
                         },
                         focus: function(event, ui){
                         $( "#autocomplete" ).val( ui.item.label );
                         return false;
                         },
               
          });

          
     });
     </script>
     <script>
          $(document).ready(function () {
               let getTblSize = $(".tbl-scrolling table tr").length;
               let getTrHeight = $(".tbl-scrolling table tr").outerHeight(true);
               x = 20;
               $('.tbl-scrolling').css('height', getTrHeight * x + 'px')
               $('.tbl-scrolling table tr:lt(' + x + ')').show();
               $('.load-more_btn').click(function () {
                    x = (x + 10 <= getTblSize) ? x + 10 : getTblSize;
                    $('.tbl-scrolling table tr:lt(' + x + ')').show();
                    $('.tbl-scrolling').css('height', 500 + getTrHeight * x + 'px');
                    if (x == getTblSize) {
                         $('.load-more_wrp').hide();
                    }
               });
               var thHeight = $("tr.bg_blue1").outerHeight(true);
               $(".jump-to_item a").click(function (e) {
                    e.preventDefault();
                    $(".jump-to_item a").removeClass("active")
                    $(this).addClass("active")
                    var container = $('.tbl-scrolling'), id = $(this).attr('href'),
                         scrollTo = $(id);
                         console.log(scrollTo);
                    container.animate({
                         scrollTop: scrollTo.offset().top - container.offset().top - thHeight + container.scrollTop()
                    });
               });

               $(".jump-to_item").on("click", function () {
                    $(".jump-to_item").removeClass("active");
                    $("this").addClass("active");
                    $(".jump-to_list").scrollCenter(".active", 300);
               });
               jQuery.fn.scrollCenter = function (elem, speed) {
                    var active = jQuery(this).find(elem);
                    var activeWidth = active.width() / 2;
                    var pos = active.position().left + activeWidth;
                    var elpos = jQuery(this).scrollLeft();
                    var elW = jQuery(this).width();
                    pos = pos + elpos - elW / 2;
                    jQuery(this).animate({
                         scrollLeft: pos
                    }, speed == undefined ? 1000 : speed);
                    return this;
               };

               jQuery.fn.scrollCenterORI = function (elem, speed) {
                    jQuery(this).animate({
                         scrollLeft: jQuery(this).scrollLeft() - jQuery(this).offset().left + jQuery(elem).offset().left
                    }, speed == undefined ? 1000 : speed);
                    return this;
               };


               (function ($) {
                    $(".jump-to_list").on('scroll', function () {
                         $val = $(this).scrollLeft();
                         if ($(this).scrollLeft() + $(this).innerWidth() >= $(this)[0].scrollWidth) {
                         $(".nav-next").hide();
                         } else {
                         $(".nav-next").show();
                         }

                         if ($val == 0) {
                         $(".nav-prev").hide();
                         } else {
                         $(".nav-prev").show();
                         }
                    });
                    console.log('init-scroll: ' + $(".nav-next").scrollLeft());
                    $(".nav-next").on("click", function () {
                         $(".jump-to_list").animate({ scrollLeft: '+=115' }, 200);

                    });
                    $(".nav-prev").on("click", function () {
                         $(".jump-to_list").animate({ scrollLeft: '-=115' }, 200);
                    });
               })(jQuery);

          });
     </script>​
                    
          </div>
               </section>
     
     <section class="pt_ds_prc mt-15 bg_blue1 p-15 b_rad4">
     <div class="tp_br d-flex ai-center mb-16">
                    <h2 class="color-blue font-22 font-w500">Petrol Price</h2>
                    <span class="dt_blk font-12 ml-10 mr-auto">Jan 30, 2024</span>

          <div class="city_selct d-flex pos-rel">
               <span class="is-block selctDsgn selctMenu_n d-flex ai-center">
                    <select id="sddropdown" onchange="chgSelect('petrol',this.options[this.selectedIndex].value, 'state');">
                         <option value="select">Select State</option>
                                             <option value="andaman-and-nicobar" >Andaman And Nicobar</option>
                                             <option value="andhra-pradesh" >Andhra Pradesh</option>
                                             <option value="arunachal-pradesh" >Arunachal Pradesh</option>
                                             <option value="assam" >Assam</option>
                                             <option value="bihar" >Bihar</option>
                                             <option value="chandigarh" >Chandigarh</option>
                                             <option value="chhattisgarh" >Chhattisgarh</option>
                                             <option value="dadra-and-nagar-haveli" >Dadra And Nagar Haveli</option>
                                             <option value="daman-and-diu" >Daman And Diu</option>
                                             <option value="delhi" >Delhi</option>
                                             <option value="goa" >Goa</option>
                                             <option value="gujarat" selected>Gujarat</option>
                                             <option value="haryana" >Haryana</option>
                                             <option value="himachal-pradesh" >Himachal Pradesh</option>
                                             <option value="jammu-and-kashmir" >Jammu And Kashmir</option>
                                             <option value="jharkhand" >Jharkhand</option>
                                             <option value="karnataka" >Karnataka</option>
                                             <option value="kerala" >Kerala</option>
                                             <option value="madhya-pradesh" >Madhya Pradesh</option>
                                             <option value="maharashtra" >Maharashtra</option>
                                             <option value="manipur" >Manipur</option>
                                             <option value="meghalaya" >Meghalaya</option>
                                             <option value="mizoram" >Mizoram</option>
                                             <option value="nagaland" >Nagaland</option>
                                             <option value="odisha" >Odisha</option>
                                             <option value="puducherry" >Puducherry</option>
                                             <option value="punjab" >Punjab</option>
                                             <option value="rajasthan" >Rajasthan</option>
                                             <option value="sikkim" >Sikkim</option>
                                             <option value="tamil-nadu" >Tamil Nadu</option>
                                             <option value="telangana" >Telangana</option>
                                             <option value="tripura" >Tripura</option>
                                             <option value="uttar-pradesh" >Uttar Pradesh</option>
                                             <option value="uttarakhand" >Uttarakhand</option>
                                             <option value="west-bengal" >West Bengal</option>
                                        </select>
               </span>
               <span class="is-block selctDsgn selctMenu_n d-flex ai-center">
                    <select id="cddropdown" onchange="chgSelect('petrol',this.options[this.selectedIndex].value, 'city');">
                         <option value="select">Select City/District</option>
                                             <option value="ahmedabad" >Ahmedabad</option>
                                             <option value="amreli" >Amreli</option>
                                             <option value="anand" >Anand</option>
                                             <option value="aravalli" >Aravalli</option>
                                             <option value="banas-kantha" >Banas Kantha</option>
                                             <option value="bharuch" >Bharuch</option>
                                             <option value="bhavnagar" selected>Bhavnagar</option>
                                             <option value="botad" >Botad</option>
                                             <option value="chhotaudepur" >Chhotaudepur</option>
                                             <option value="dahod" >Dahod</option>
                                             <option value="devbhumi-dwarka" >Devbhumi Dwarka</option>
                                             <option value="gandhi-nagar" >Gandhi Nagar</option>
                                             <option value="gir-somnath" >Gir Somnath</option>
                                             <option value="jamnagar" >Jamnagar</option>
                                             <option value="junagadh" >Junagadh</option>
                                             <option value="kheda" >Kheda</option>
                                             <option value="kutch" >Kutch</option>
                                             <option value="mahisagar" >Mahisagar</option>
                                             <option value="mehsana" >Mehsana</option>
                                             <option value="morbi" >Morbi</option>
                                             <option value="narmada" >Narmada</option>
                                             <option value="navsari" >Navsari</option>
                                             <option value="panch-mahal" >Panch Mahal</option>
                                             <option value="patan" >Patan</option>
                                             <option value="porbander" >Porbander</option>
                                             <option value="rajkot" >Rajkot</option>
                                             <option value="sabar-kantha" >Sabar Kantha</option>
                                             <option value="surat" >Surat</option>
                                             <option value="surendranagar" >Surendranagar</option>
                                             <option value="tapi" >Tapi</option>
                                             <option value="the-dangs" >The Dangs</option>
                                             <option value="vadodara" >Vadodara</option>
                                             <option value="valsad" >Valsad</option>
                                        </select>
               </span>
          </div>
     </div>

     <div class="tabs_cont mt-20">
          <div class="tb-bar ">
               <ul class="d-flex jc-center">
                    <li class="active">
                                             <a class="is-block" href="https://www.ndtv.com/fuel-prices/petrol-price-in-bhavnagar-city">Petrol(₹/L)<span class="is-block"><i class="arw_bg grn">97.77</i><i class="bgBx grnBx">0.77</i></span></a></li>
                    <li >
                                             <a class="is-block" href="https://www.ndtv.com/fuel-prices/diesel-price-in-bhavnagar-city">Diesel (₹/L)<span class="is-block"><i class="arw_bg grn">93.52</i><i class="bgBx grnBx">0.77</i></span></a></li>
               </ul>
          </div>
          <div class="tb-data-outer p-15 bg-wht pos-rel">
               <div class="tb-data" id="petrol-price-container">
                    <div class="tb-data-con">
                         <div class="chart-container">
                         <div id="petrol-price" class="chartMain mt-10"></div>
                         </div>
                    </div>
               </div>
          </div>
     </div>
     </section>

     <script src="https://www.ndtv.com/dstatic/js/highcharts.js?20220815-4"></script>
     <script>
     Highcharts.chart('petrol-price', {
          chart: {
               type: 'line',
               spacing: [10, 0, 5, 0],
               style: {
                    fontFamily: '-apple-system, Roboto, Arial, Helvetica'
               }
          },
          title: {
               text: null
          },
          credits: {enabled: false},
          subtitle: {
               text: null
          },
          xAxis: {
               categories: ["Jan 21","Jan 22","Jan 23","Jan 24","Jan 25","Jan 26","Jan 27","Jan 28","Jan 29","Jan 30"]        },
          yAxis: {
               title: {
                    text: null
               }
          },
          legend: {
               enabled: false,
               itemStyle: {
                    fontSize: '15px'
               }
          },
          plotOptions: {
               series: {
                    marker: {
                         fillColor: '#FFFFFF',
                         lineWidth: 2,
                         radius: 5,
                         lineColor: null // inherit from series
                    }
               },
               line: {
                    dataLabels: {
                         enabled: true,
                         y: -10,
                         style: {fontSize: '12px',fontWeight: 'normal'}
                    },
                    enableMouseTracking: false
               }
          },
          responsive: {
               rules: [{
                    condition: {
                         maxWidth: 500
                    },
                    chartOptions: {
                              plotOptions: {
                                   line: {
                                        dataLabels: {
                                             enabled: false,
                                        },
                                        enableMouseTracking: true
                                   },
                              }
                    }
               }]
          },
          series: [{
                    name: 'Petrol',
                    color: '#003291',
                    data: [97.67,98.25,98.1,97.99,98.1,97.77,98.48,98.1,98.54,97.77]            }]
     });
     </script>
     <script> 
     $(document).ready(function(){
     $("#sddropdown").select2(); 
     $("#cddropdown").select2(); 
     }); 
     </script>      <section class="pt_ds_prc bg_blue1 p-15 b_rad10 mtb-20">

                    <div class="fuel-tabs">
                         
                                             
                         <div class="fuel-tab">
                         
                         <label  class="fuel-tab-label is-open"  for="chck1">
                                                  Trend Of Petrol Rate In Bhavnagar, January 2024                                                </label>
                         
                                   <div class="fuel-tab-content bg-wht" style="max-height:100%;">
                                                            
                              
                              <div class="tb-data-outer p-15 b_rad4 bg-wht pos-rel">
                                   
                                   <div class="tb-data-con">
                                        <div class="tbl-container b_rad4 overflow-hidden">
                                             <table width="100%" class="font-16 color-blue prc-tble-dtls" border="0" cellspacing="0" cellpadding="0">
                                             <tbody>
                                                  <tr class="bg_blue1">
                                                       <th scope="col"></th>
                                                       <th scope="col">Petrol price</th>
                                                  </tr>
                                                  <tr>
                                                       <td>1st January</td>
                                                       <td>Rs. 98.48</td>
                                                  </tr>

                                                  <tr>
                                                       <td>30th January</td>
                                                       <td>Rs. 97.77</td>
                                                  </tr>

                                                  <tr>
                                                       <td> Highest Rate In January </td>
                                                       
                                                       <td>Rs. 98.54 on January 2nd</td>
                                                  </tr>

                                                  <tr>
                                                       <td> Lowest Rate In January </td>
                                                       <td>Rs. 97.67 on January 21st</td>
                                                  </tr>

                                                  <tr>
                                                       <td>Over all performance</td>
                                                       <td>Falling</td>
                                                  </tr>

                                                  <tr>
                                                       <td>% Change </td>
                                                       <td><span class="prc-up_txt" >-0.89</span></td>
                                                  </tr>
                                             </tbody>
                                             </table>
                                        </div>
                                                  <p><b>Monthly Fuel Price Trend In Bhavnagar For January 2024:</b></p>
                                   
                    
                                                  <p>- Petrol price in Bhavnagar started in January at Rs 98.48 per litre, 
                              after rising 0.43 per cent                          from the previous month's close of Rs 98.06 per litre.</p>
                              
     <p>- The highest recorded rate for Petrol during January was Rs.98.54,  
          an 0.88 per cent rise between                                                  1st January and 30th January.<p/>

     <p>- The lowest recorded rate for Petrol during January was Rs.97.67,  
          an 0.89 per cent fall between                                                  1st January and 30th January.<p/>

     <p>- Petrol prices closed out 30th January at Rs 97.77 per litre, 
          a fall of 0.89 per cent in the month.                         </p>
                         </div>
                         </div>
                         </div>
                         </div>
                                             
                         <div class="fuel-tab">
                         
                         <label class="fuel-tab-label" for="chck2">
                                                  Trend Of Petrol Rate In Bhavnagar, December 2023                                                </label>
                         
                                   <div class="fuel-tab-content bg-wht" >
                                                            
                              
                              <div class="tb-data-outer p-15 b_rad4 bg-wht pos-rel">
                                   
                                   <div class="tb-data-con">
                                        <div class="tbl-container b_rad4 overflow-hidden">
                                             <table width="100%" class="font-16 color-blue prc-tble-dtls" border="0" cellspacing="0" cellpadding="0">
                                             <tbody>
                                                  <tr class="bg_blue1">
                                                       <th scope="col"></th>
                                                       <th scope="col">Petrol price</th>
                                                  </tr>
                                                  <tr>
                                                       <td>1st December</td>
                                                       <td>Rs. 97.99</td>
                                                  </tr>

                                                  <tr>
                                                       <td>31st December</td>
                                                       <td>Rs. 98.06</td>
                                                  </tr>

                                                  <tr>
                                                       <td> Highest Rate In December </td>
                                                       
                                                       <td>Rs. 98.83 on December 15th</td>
                                                  </tr>

                                                  <tr>
                                                       <td> Lowest Rate In December </td>
                                                       <td>Rs. 97.66 on December 24th</td>
                                                  </tr>

                                                  <tr>
                                                       <td>Over all performance</td>
                                                       <td>Falling</td>
                                                  </tr>

                                                  <tr>
                                                       <td>% Change </td>
                                                       <td><span class="prc-up_txt" >-1.20</span></td>
                                                  </tr>
                                             </tbody>
                                             </table>
                                        </div>
                                                  <p><b>Monthly Fuel Price Trend In Bhavnagar For December 2023:</b></p>
                                   
                    
                                                  <p>- Petrol price in Bhavnagar started in December at Rs 97.99 per litre, 
                              after falling 0.86 per cent                          from the previous month's close of Rs 98.83 per litre.</p>
                              
     <p>- The highest recorded rate for Petrol during December was Rs.98.83,  
          an 1.18 per cent rise between                                                  1st December and 31st December.<p/>

     <p>- The lowest recorded rate for Petrol during December was Rs.97.66,  
          an 1.2 per cent fall between                                                  1st December and 31st December.<p/>

     <p>- Petrol prices closed out 31st December at Rs 98.06 per litre, 
          a fall of 1.2 per cent in the month.                         </p>
                         </div>
                         </div>
                         </div>
                         </div>
                                             
                         <div class="fuel-tab">
                         
                         <label class="fuel-tab-label" for="chck3">
                                                  Trend Of Petrol Rate In Bhavnagar, November 2023                                                </label>
                         
                                   <div class="fuel-tab-content bg-wht" >
                                                            
                              
                              <div class="tb-data-outer p-15 b_rad4 bg-wht pos-rel">
                                   
                                   <div class="tb-data-con">
                                        <div class="tbl-container b_rad4 overflow-hidden">
                                             <table width="100%" class="font-16 color-blue prc-tble-dtls" border="0" cellspacing="0" cellpadding="0">
                                             <tbody>
                                                  <tr class="bg_blue1">
                                                       <th scope="col"></th>
                                                       <th scope="col">Petrol price</th>
                                                  </tr>
                                                  <tr>
                                                       <td>1st November</td>
                                                       <td>Rs. 98.83</td>
                                                  </tr>

                                                  <tr>
                                                       <td>30th November</td>
                                                       <td>Rs. 98.83</td>
                                                  </tr>

                                                  <tr>
                                                       <td> Highest Rate In November </td>
                                                       
                                                       <td>Rs. 98.83 on November 1st</td>
                                                  </tr>

                                                  <tr>
                                                       <td> Lowest Rate In November </td>
                                                       <td>Rs. 97.66 on November 5th</td>
                                                  </tr>

                                                  <tr>
                                                       <td>Over all performance</td>
                                                       <td>Falling</td>
                                                  </tr>

                                                  <tr>
                                                       <td>% Change </td>
                                                       <td><span class="prc-up_txt" >-1.20</span></td>
                                                  </tr>
                                             </tbody>
                                             </table>
                                        </div>
                                                  <p><b>Monthly Fuel Price Trend In Bhavnagar For November 2023:</b></p>
                                   
                    
                                                  <p>- Petrol price in Bhavnagar started in November at Rs 98.83 per litre, 
                              after rising 1 per cent                          from the previous month's close of Rs 97.84 per litre.</p>
                              
     <p>- The highest recorded rate for Petrol during November was Rs.98.83,  
          an 1.18 per cent rise between                                                  1st November and 30th November.<p/>

     <p>- The lowest recorded rate for Petrol during November was Rs.97.66,  
          an 1.2 per cent fall between                                                  1st November and 30th November.<p/>

     <p>- Petrol prices closed out 30th November at Rs 98.83 per litre, 
          a fall of 1.2 per cent in the month.                         </p>
                         </div>
                         </div>
                         </div>
                         </div>
                                             
                         <div class="fuel-tab">
                         
                         <label class="fuel-tab-label" for="chck4">
                                                  Trend Of Petrol Rate In Bhavnagar, October 2023                                                </label>
                         
                                   <div class="fuel-tab-content bg-wht" >
                                                            
                              
                              <div class="tb-data-outer p-15 b_rad4 bg-wht pos-rel">
                                   
                                   <div class="tb-data-con">
                                        <div class="tbl-container b_rad4 overflow-hidden">
                                             <table width="100%" class="font-16 color-blue prc-tble-dtls" border="0" cellspacing="0" cellpadding="0">
                                             <tbody>
                                                  <tr class="bg_blue1">
                                                       <th scope="col"></th>
                                                       <th scope="col">Petrol price</th>
                                                  </tr>
                                                  <tr>
                                                       <td>1st October</td>
                                                       <td>Rs. 98.06</td>
                                                  </tr>

                                                  <tr>
                                                       <td>31st October</td>
                                                       <td>Rs. 97.84</td>
                                                  </tr>

                                                  <tr>
                                                       <td> Highest Rate In October </td>
                                                       
                                                       <td>Rs. 98.61 on October 16th</td>
                                                  </tr>

                                                  <tr>
                                                       <td> Lowest Rate In October </td>
                                                       <td>Rs. 97.77 on October 4th</td>
                                                  </tr>

                                                  <tr>
                                                       <td>Over all performance</td>
                                                       <td>Rising</td>
                                                  </tr>

                                                  <tr>
                                                       <td>% Change </td>
                                                       <td><span class="prc-down_txt" >+0.85</span></td>
                                                  </tr>
                                             </tbody>
                                             </table>
                                        </div>
                                                  <p><b>Monthly Fuel Price Trend In Bhavnagar For October 2023:</b></p>
                                   
                    
                                                  <p>- Petrol price in Bhavnagar started in October at Rs 98.06 per litre, 
                              after rising 0.3 per cent                          from the previous month's close of Rs 97.77 per litre.</p>
                              
     <p>- The highest recorded rate for Petrol during October was Rs.98.61,  
          an 0.85 per cent rise between                                                  1st October and 31st October.<p/>

     <p>- The lowest recorded rate for Petrol during October was Rs.97.77,  
          an 0.86 per cent fall between                                                  1st October and 31st October.<p/>

     <p>- Petrol prices closed out 31st October at Rs 97.84 per litre, 
          a rise of 0.85 per cent in the month.                         </p>
                         </div>
                         </div>
                         </div>
                         </div>
                                             
                         <div class="fuel-tab">
                         
                         <label class="fuel-tab-label" for="chck5">
                                                  Trend Of Petrol Rate In Bhavnagar, September 2023                                                </label>
                         
                                   <div class="fuel-tab-content bg-wht" >
                                                            
                              
                              <div class="tb-data-outer p-15 b_rad4 bg-wht pos-rel">
                                   
                                   <div class="tb-data-con">
                                        <div class="tbl-container b_rad4 overflow-hidden">
                                             <table width="100%" class="font-16 color-blue prc-tble-dtls" border="0" cellspacing="0" cellpadding="0">
                                             <tbody>
                                                  <tr class="bg_blue1">
                                                       <th scope="col"></th>
                                                       <th scope="col">Petrol price</th>
                                                  </tr>
                                                  <tr>
                                                       <td>1st September</td>
                                                       <td>Rs. 98.48</td>
                                                  </tr>

                                                  <tr>
                                                       <td>30th September</td>
                                                       <td>Rs. 97.77</td>
                                                  </tr>

                                                  <tr>
                                                       <td> Highest Rate In September </td>
                                                       
                                                       <td>Rs. 98.61 on September 10th</td>
                                                  </tr>

                                                  <tr>
                                                       <td> Lowest Rate In September </td>
                                                       <td>Rs. 97.66 on September 18th</td>
                                                  </tr>

                                                  <tr>
                                                       <td>Over all performance</td>
                                                       <td>Falling</td>
                                                  </tr>

                                                  <tr>
                                                       <td>% Change </td>
                                                       <td><span class="prc-up_txt" >-0.97</span></td>
                                                  </tr>
                                             </tbody>
                                             </table>
                                        </div>
                                                  <p><b>Monthly Fuel Price Trend In Bhavnagar For September 2023:</b></p>
                                   
                    
                                                  <p>- Petrol price in Bhavnagar started in September at Rs 98.48 per litre, 
                              after falling 0.06 per cent                          from the previous month's close of Rs 98.54 per litre.</p>
                              
     <p>- The highest recorded rate for Petrol during September was Rs.98.61,  
          an 0.96 per cent rise between                                                  1st September and 30th September.<p/>

     <p>- The lowest recorded rate for Petrol during September was Rs.97.66,  
          an 0.97 per cent fall between                                                  1st September and 30th September.<p/>

     <p>- Petrol prices closed out 30th September at Rs 97.77 per litre, 
          a fall of 0.97 per cent in the month.                         </p>
                         </div>
                         </div>
                         </div>
                         </div>
                                             
                         <div class="fuel-tab">
                         
                         <label class="fuel-tab-label" for="chck6">
                                                  Trend Of Petrol Rate In Bhavnagar, August 2023                                                </label>
                         
                                   <div class="fuel-tab-content bg-wht" >
                                                            
                              
                              <div class="tb-data-outer p-15 b_rad4 bg-wht pos-rel">
                                   
                                   <div class="tb-data-con">
                                        <div class="tbl-container b_rad4 overflow-hidden">
                                             <table width="100%" class="font-16 color-blue prc-tble-dtls" border="0" cellspacing="0" cellpadding="0">
                                             <tbody>
                                                  <tr class="bg_blue1">
                                                       <th scope="col"></th>
                                                       <th scope="col">Petrol price</th>
                                                  </tr>
                                                  <tr>
                                                       <td>1st August</td>
                                                       <td>Rs. 98.54</td>
                                                  </tr>

                                                  <tr>
                                                       <td>31st August</td>
                                                       <td>Rs. 98.54</td>
                                                  </tr>

                                                  <tr>
                                                       <td> Highest Rate In August </td>
                                                       
                                                       <td>Rs. 98.83 on August 19th</td>
                                                  </tr>

                                                  <tr>
                                                       <td> Lowest Rate In August </td>
                                                       <td>Rs. 97.66 on August 12th</td>
                                                  </tr>

                                                  <tr>
                                                       <td>Over all performance</td>
                                                       <td>Rising</td>
                                                  </tr>

                                                  <tr>
                                                       <td>% Change </td>
                                                       <td><span class="prc-down_txt" >+1.18</span></td>
                                                  </tr>
                                             </tbody>
                                             </table>
                                        </div>
                                                  <p><b>Monthly Fuel Price Trend In Bhavnagar For August 2023:</b></p>
                                   
                    
                                                  <p>- Petrol price in Bhavnagar started in August at Rs 98.54 per litre, 
                              remaining unchanged from the previous month's close of Rs 98.54 per litre.</p>
                              
     <p>- The highest recorded rate for Petrol during August was Rs.98.83,  
          an 1.18 per cent rise between                                                  1st August and 31st August.<p/>

     <p>- The lowest recorded rate for Petrol during August was Rs.97.66,  
          an 1.2 per cent fall between                                                  1st August and 31st August.<p/>

     <p>- Petrol prices closed out 31st August at Rs 98.54 per litre, 
          a rise of 1.18 per cent in the month.                         </p>
                         </div>
                         </div>
                         </div>
                         </div>
                                             
                         <div class="fuel-tab">
                         
                         <label class="fuel-tab-label" for="chck7">
                                                  Trend Of Petrol Rate In Bhavnagar, July 2023                                                </label>
                         
                                   <div class="fuel-tab-content bg-wht" >
                                                            
                              
                              <div class="tb-data-outer p-15 b_rad4 bg-wht pos-rel">
                                   
                                   <div class="tb-data-con">
                                        <div class="tbl-container b_rad4 overflow-hidden">
                                             <table width="100%" class="font-16 color-blue prc-tble-dtls" border="0" cellspacing="0" cellpadding="0">
                                             <tbody>
                                                  <tr class="bg_blue1">
                                                       <th scope="col"></th>
                                                       <th scope="col">Petrol price</th>
                                                  </tr>
                                                  <tr>
                                                       <td>1st July</td>
                                                       <td>Rs. 97.84</td>
                                                  </tr>

                                                  <tr>
                                                       <td>31st July</td>
                                                       <td>Rs. 98.54</td>
                                                  </tr>

                                                  <tr>
                                                       <td> Highest Rate In July </td>
                                                       
                                                       <td>Rs. 98.83 on July 18th</td>
                                                  </tr>

                                                  <tr>
                                                       <td> Lowest Rate In July </td>
                                                       <td>Rs. 97.66 on July 3rd</td>
                                                  </tr>

                                                  <tr>
                                                       <td>Over all performance</td>
                                                       <td>Rising</td>
                                                  </tr>

                                                  <tr>
                                                       <td>% Change </td>
                                                       <td><span class="prc-down_txt" >+1.18</span></td>
                                                  </tr>
                                             </tbody>
                                             </table>
                                        </div>
                                                  <p><b>Monthly Fuel Price Trend In Bhavnagar For July 2023:</b></p>
                                   
                    
                                                  <p>- Petrol price in Bhavnagar started in July at Rs 97.84 per litre, 
                              after rising 0.07 per cent                          from the previous month's close of Rs 97.77 per litre.</p>
                              
     <p>- The highest recorded rate for Petrol during July was Rs.98.83,  
          an 1.18 per cent rise between                                                  1st July and 31st July.<p/>

     <p>- The lowest recorded rate for Petrol during July was Rs.97.66,  
          an 1.2 per cent fall between                                                  1st July and 31st July.<p/>

     <p>- Petrol prices closed out 31st July at Rs 98.54 per litre, 
          a rise of 1.18 per cent in the month.                         </p>
                         </div>
                         </div>
                         </div>
                         </div>
                                        </div>

     </section>

     <script>
     const accordionBtns = document.querySelectorAll(".fuel-tab-label");
     accordionBtns.forEach((accordion) => {
     accordion.onclick = function () {
     this.classList.toggle("is-open");
     let content = this.nextElementSibling;
     if (content.style.maxHeight) {
          content.style.maxHeight = null;
     } else {
          content.style.maxHeight = content.scrollHeight + "px";
     }
     };
     });
     </script>      
     <div class="stry-head mt-20">
                    <h2 class="stry-ttl"> <a href="javascript:void()">Related News For</a> </h2>
                    
               </div>

               <section class="pt_ds_prc bg_blue1 p-15 b_rad10 mb-16">
                    <div class="tp_br d-flex ai-center">
                         <div class="tb-data-outer p-15 b_rad4 bg-wht pos-rel">
                              <div class="stry-wrp">
                              <ul class="stry-list">
                                                                 <li class="stry-item">
                                        <span class="stry-img_thumb">
                                             <a class="stry-link" href="https://www.ndtv.com/india-news/20-years-after-car-purchase-maruti-suzuki-fined-for-misleading-mileage-claims-4937498" target="_blank"> <img src="https://c.ndtvimg.com/2024-01/2teg9kig_maruti-suzuki-zen_625x300_26_January_24.jpeg" loading="lazy" alt="petrol news" title="20 Years After Car Purchase, Maruti Suzuki Fined for Misleading Mileage Claims"> </a>
                                        </span>
                                        <h3 class="stry-head_ttl">
                                             <a class="stry-link" href="https://www.ndtv.com/india-news/20-years-after-car-purchase-maruti-suzuki-fined-for-misleading-mileage-claims-4937498" target="_blank" alt="petrol news">20 Years After Car Purchase, Maruti Suzuki Fined for Misleading Mileage Claims </a>
                                        </h3>
                                   </li>
                                                                 <li class="stry-item">
                                        <span class="stry-img_thumb">
                                             <a class="stry-link" href="https://www.ndtv.com/world-news/ron-desantis-from-rising-star-to-failed-white-house-hopeful-4907829" target="_blank"> <img src="https://c.ndtvimg.com/2024-01/mcbocij8_ron-desantis-afp_625x300_22_January_24.jpg?im=FaceCrop,algorithm=dnn,width=240,height=180" loading="lazy" alt="petrol news" title="Ron DeSantis, From Rising Star To Failed White House Hopeful"> </a>
                                        </span>
                                        <h3 class="stry-head_ttl">
                                             <a class="stry-link" href="https://www.ndtv.com/world-news/ron-desantis-from-rising-star-to-failed-white-house-hopeful-4907829" target="_blank" alt="petrol news">Ron DeSantis, From Rising Star To Failed White House Hopeful </a>
                                        </h3>
                                   </li>
                                                                 <li class="stry-item">
                                        <span class="stry-img_thumb">
                                             <a class="stry-link" href="https://www.ndtv.com/offbeat/mans-note-taking-method-during-fight-fuels-girlfriends-fury-internet-offers-advice-4874852" target="_blank"> <img src="https://c.ndtvimg.com/2024-01/e274mjfo_notes-generic_625x300_16_January_24.jpeg" loading="lazy" alt="petrol news" title="Man's Note-Taking Method During Fight Fuels Girlfriend's Fury. Internet Offers Advice"> </a>
                                        </span>
                                        <h3 class="stry-head_ttl">
                                             <a class="stry-link" href="https://www.ndtv.com/offbeat/mans-note-taking-method-during-fight-fuels-girlfriends-fury-internet-offers-advice-4874852" target="_blank" alt="petrol news">Man's Note-Taking Method During Fight Fuels Girlfriend's Fury. Internet Offers Advice </a>
                                        </h3>
                                   </li>
                                                                 <li class="stry-item">
                                        <span class="stry-img_thumb">
                                             <a class="stry-link" href="https://www.ndtv.com/world-news/ai-to-impact-60-jobs-in-advanced-economies-says-imf-chief-kristalina-georgieva-4864334" target="_blank"> <img src="https://c.ndtvimg.com/2022-10/7ladmd14_kristalina-georgieva_120x90_03_October_22.jpg" loading="lazy" alt="petrol news" title=""Your Job May Disappear Altogether, Or...": IMF Chief On AI Impact"> </a>
                                        </span>
                                        <h3 class="stry-head_ttl">
                                             <a class="stry-link" href="https://www.ndtv.com/world-news/ai-to-impact-60-jobs-in-advanced-economies-says-imf-chief-kristalina-georgieva-4864334" target="_blank" alt="petrol news">"Your Job May Disappear Altogether, Or...": IMF Chief On AI Impact </a>
                                        </h3>
                                   </li>
                                   
                              
                              </ul>

                              </div>
                         </div>
                         </div>
               </section>    <section class="pg_copy">
          <p>As of June 2017, petrol prices in India are revised daily, and this is called the dynamic fuel price method. Petrol and diesel rates are revised at 06:00 am every day. Before this, prices were revised every fortnight. Various factors impact the price of fuel, these include the Rupee to US dollar exchange rate, cost of crude oil, global cues, demand for fuel, and so on. When international crude oil prices gain, prices in India move higher. The price of fuel includes excise duty, value-added tax (VAT), and dealer commission. VAT varies from state to state. After adding excise duty, dealer commission and VAT, the retail selling price of the petrol gets nearly doubled.</p>    </section>

     </main>
     <script> 
     $(document).ready(function(){
     $("#sdropdown").select2(); 
     $("#cdropdown").select2(); 
     }); 
     </script>                  <div class="taboola-new-wrp">
          <div id="taboola-below-article-thumbnails"></div>
     <script type="text/javascript">
          window._rrCode = window._rrCode || [];_rrCode.push(function(){ 
          window._taboola = window._taboola || [];
          _taboola.push({
               mode: 'thumbnails-c',
               container: 'taboola-below-article-thumbnails',
               placement: 'Below Section Thumbnails Fuel-update',
               target_type: 'mix'
          });
          }); 
     </script>
     <script type="text/javascript">
          window._rrCode = window._rrCode || [];_rrCode.push(function(){ 
          window._taboola = window._taboola || [];
          _taboola.push({category: 'auto'});
          _taboola.push({flush: true});
          }); 
     </script>
     </div>
               
          
          <footer class="font-13 t-center p-10">&copy; COPYRIGHT NDTV CONVERGENCE LIMITED 2024. ALL RIGHTS RESERVED.</footer>
               </div>
     <div class="sbMenu_bg">
          <div class="sbMenu_sideDv height100p">
               <div class="sbMenu bg-wht">
                    <div class="main_logo">
                         <a href="#" class="is-block"></a>
                         <span class="logo-text font-12 t-uppercase font-b">
                         <i class="font_s-n is-block">Calculator</i>
                         </span>
                    </div>
               </div>
          </div>
     </div>
     <div class="ntfPanel w-100 height100p">
          <div class="ntfPanel__bg"></div>
          <div class="w-100 height100p d-flex jc-center ai-center">
               <div class="ntfPanel__cn bg-wht pos-rel">
                    <i class="iconContnr"></i>
                    <span class="crs-btn"></span>
                    <h3>Subscribe for notifications</h3>
                    <div class="fieldContnr">
                         <div class="alert error success font-14 mb-10" id="__msg"></div>
                         <div class="field-row">
                         <div class="fieldinput emailIcn pos-rel d-flex">
                              <input class="font-16 pr-10 b_rad4 pl-15 typeField" id="__usrEmail" type="email" placeholder="Email*" title="Please Provide A Valid Email Address !" />
                         </div>
                         </div>
                         <div class="field-row mt-20">
                         <div class="fieldinput mobileIcn pos-rel mb-5 d-flex">
                              <input class="font-16 pr-10 b_rad4 pl-15 typeField" id="__usrMobile" type="text" pattern="[0-9]{10}" maxlength="10" placeholder="Mobile (987654321)" value=""/>
                         </div>
                         </div>

                         <div class="fieldinput mtb-20">
                         <input type="hidden" id="__type" value="" />
                         <input type="button" class="font-16 font-b prl-20 w-100" onclick="usrSubs();" value="Subscribe me" />
                         </div>
                         <div class="b_t_dash1 field-row mt-15 pt-20 brwsrPush is-hidden">
                         <div class="fieldinput pos-rel">
                              <input type="button" id="subsBtn" class="font-16 font-b prl-20 w-100 t-left" value="Subscribe browser alert">
                              <span class="tickIcn b_rad4"></span>
                         </div>
                         </div>
                    </div>
               </div>
          </div>
     </div>
          <!-- [Side Nav] -->
          <div class="sid-nav">
          <div class="sid-nav-wrp">
               <div class="snv_cn-hed">
                    <!-- Logo -->
                    <a class="ndtv-logo" href="https://www.ndtv.com">
                         <img class="ndtv-lgo_img"
                         src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48c3ZnIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4IiB2aWV3Qm94PSIwIDAgMzY1IDY4LjkiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDM2NSA2OC45OyIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+PHN0eWxlIHR5cGU9InRleHQvY3NzIj4uc3Qwe2ZpbGw6I0VFMDAwMDt9PC9zdHlsZT48ZyBpZD0iWE1MSURfMV8iPjxwYXRoIGlkPSJYTUxJRF8zXyIgZD0iTTAsMC4xYzguNCwwLDE2LjgtMC4xLDI1LjIsMEMzNS4yLDAuNyw0NCw3LjQsNDguOCwxNmM0LjgsOS4xLDksMTguNSwxMy45LDI3LjVjMS42LDMuMiw0LjgsNS40LDguNCw1LjVDNzAuOSwzMi43LDcxLDE2LjQsNzEsMGM3LjQsMC4xLDE0LjcsMCwyMi4xLDBjMCw3LjEsMCwxNC4yLTAuMSwyMS40Yy01LjEsMi05LjQsNi41LTkuNSwxMi4yYy0wLjcsNi4yLDMuOSwxMS44LDkuNSwxMy43YzAuMSw3LjIsMCwxNC4zLDAuMSwyMS41Yy03LjMsMC4xLTE0LjcsMC0yMiwwLjFjLTguNSwwLjQtMTYuOS0zLjUtMjIuMy05LjljLTYtNy4zLTkuMS0xNi41LTEzLjYtMjQuNkMzMi4xLDI4LjYsMjkuOSwyMCwyMiwxOS43YzAsMTYuNC0wLjEsMzIuNywwLjEsNDkuMWMtNy40LDAuMS0xNC43LDAuMS0yMi4xLDBDMC4xLDQ1LjksMC4xLDIzLDAsMC4xeiIvPjxwYXRoIGlkPSJYTUxJRF82XyIgZD0iTTk5LjYsMC4xYzYyLjQsMCwxMjQuNy0wLjIsMTg3LjEsMC4xYzkuMywxNi45LDE4LjgsMzMuNywyOCw1MC42YzkuMi0xNi44LDE3LjctMzQsMjYuOC01MC44YzcuOCwwLjEsMTUuNi0wLjEsMjMuNSwwLjJjLTEuMywxLjktMi42LDMuOC0zLjcsNS44Yy0xMSwyMS0yMi4xLDQxLjktMzMuMiw2Mi44Yy04LjksMC0xNy45LDAtMjYuOCwwYy05LjctMTcuNS0xOS42LTM1LTI5LjItNTIuNWMtOS44LTAuMS0xOS43LDAtMjkuNSwwYzAsMTcuNSwwLjEsMzUsMCw1Mi41Yy03LjEsMC0xNC4xLDAtMjEuMiwwYzAtMTcuNSwwLjEtMzUsMC01Mi42Yy0xMC44LDAuMS0yMS43LDAtMzIuNSwwLjFjMiw3LjUsMS44LDE1LjMsMS41LDIzYy0wLjMsNy44LTIuNCwxNi4yLTguMiwyMS44Yy01LjYsNS44LTE0LDcuOC0yMS44LDcuN2MtMjAuMi0wLjEtNDAuNCwwLjEtNjAuNS0wLjFjMC4xLTcuMiwwLTE0LjMsMC4xLTIxLjRjNC44LTEuOSw4LjktNS44LDkuNC0xMS4yYzEtNi41LTMuNS0xMi42LTkuNC0xNC43Qzk5LjYsMTQuMyw5OS44LDcuMiw5OS42LDAuMSBNMTIxLjEsMTYuNWMwLjIsMTIsMC4xLDIzLjksMC4xLDM1LjljMTIuMSwwLjIsMjQuMiwwLjEsMzYuMiwwLjFjNC43LDAuMiwxMC4zLTIuNCwxMS03LjZjMC40LTYuNywwLjMtMTMuNCwwLjEtMjAuMWMtMC41LTUuNC02LjEtOC40LTExLjEtOC4zQzE0NS4zLDE2LjMsMTMzLjIsMTYuMiwxMjEuMSwxNi41eiIvPjxwYXRoIGlkPSJYTUxJRF83XyIgY2xhc3M9InN0MCIgZD0iTTgzLjUsMzMuNmMwLjEtNS43LDQuNC0xMC4zLDkuNS0xMi4yYzIuMi0wLjIsNC41LTAuMiw2LjcsMGM1LjksMi4yLDEwLjQsOC4yLDkuNCwxNC43Yy0wLjQsNS4zLTQuNiw5LjMtOS40LDExLjJjLTIuMiwwLjItNC41LDAuMi02LjcsMEM4Ny40LDQ1LjQsODIuOCwzOS45LDgzLjUsMzMuNnoiLz48L2c+PC9zdmc+">
                         <img class="ndtv-lgo_img-lg"
                         src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDI0LjEuMCwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPgo8c3ZnIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4IgoJIHZpZXdCb3g9IjAgMCAzNjUgNjguOSIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgMzY1IDY4Ljk7IiB4bWw6c3BhY2U9InByZXNlcnZlIj4KPHN0eWxlIHR5cGU9InRleHQvY3NzIj4KCS5zdDB7ZmlsbDojRkZGRkZGO30KCS5zdDF7ZmlsbDojRUUwMDAwO30KPC9zdHlsZT4KPGcgaWQ9IlhNTElEXzFfIj4KCTxwYXRoIGlkPSJYTUxJRF8zXyIgY2xhc3M9InN0MCIgZD0iTTAsMC4xYzguNCwwLDE2LjgtMC4xLDI1LjIsMEMzNS4yLDAuNyw0NCw3LjQsNDguOCwxNmM0LjgsOS4xLDksMTguNSwxMy45LDI3LjUKCQljMS42LDMuMiw0LjgsNS40LDguNCw1LjVDNzAuOSwzMi43LDcxLDE2LjQsNzEsMGM3LjQsMC4xLDE0LjcsMCwyMi4xLDBjMCw3LjEsMCwxNC4yLTAuMSwyMS40Yy01LjEsMi05LjQsNi41LTkuNSwxMi4yCgkJYy0wLjcsNi4yLDMuOSwxMS44LDkuNSwxMy43YzAuMSw3LjIsMCwxNC4zLDAuMSwyMS41Yy03LjMsMC4xLTE0LjcsMC0yMiwwLjFjLTguNSwwLjQtMTYuOS0zLjUtMjIuMy05LjkKCQljLTYtNy4zLTkuMS0xNi41LTEzLjYtMjQuNkMzMi4xLDI4LjYsMjkuOSwyMCwyMiwxOS43YzAsMTYuNC0wLjEsMzIuNywwLjEsNDkuMWMtNy40LDAuMS0xNC43LDAuMS0yMi4xLDBDMC4xLDQ1LjksMC4xLDIzLDAsMC4xeiIKCQkvPgoJPHBhdGggaWQ9IlhNTElEXzZfIiBjbGFzcz0ic3QwIiBkPSJNOTkuNiwwLjFjNjIuNCwwLDEyNC43LTAuMiwxODcuMSwwLjFjOS4zLDE2LjksMTguOCwzMy43LDI4LDUwLjZjOS4yLTE2LjgsMTcuNy0zNCwyNi44LTUwLjgKCQljNy44LDAuMSwxNS42LTAuMSwyMy41LDAuMmMtMS4zLDEuOS0yLjYsMy44LTMuNyw1LjhjLTExLDIxLTIyLjEsNDEuOS0zMy4yLDYyLjhjLTguOSwwLTE3LjksMC0yNi44LDAKCQljLTkuNy0xNy41LTE5LjYtMzUtMjkuMi01Mi41Yy05LjgtMC4xLTE5LjcsMC0yOS41LDBjMCwxNy41LDAuMSwzNSwwLDUyLjVjLTcuMSwwLTE0LjEsMC0yMS4yLDBjMC0xNy41LDAuMS0zNSwwLTUyLjYKCQljLTEwLjgsMC4xLTIxLjcsMC0zMi41LDAuMWMyLDcuNSwxLjgsMTUuMywxLjUsMjNjLTAuMyw3LjgtMi40LDE2LjItOC4yLDIxLjhjLTUuNiw1LjgtMTQsNy44LTIxLjgsNy43CgkJYy0yMC4yLTAuMS00MC40LDAuMS02MC41LTAuMWMwLjEtNy4yLDAtMTQuMywwLjEtMjEuNGM0LjgtMS45LDguOS01LjgsOS40LTExLjJjMS02LjUtMy41LTEyLjYtOS40LTE0LjcKCQlDOTkuNiwxNC4zLDk5LjgsNy4yLDk5LjYsMC4xIE0xMjEuMSwxNi41YzAuMiwxMiwwLjEsMjMuOSwwLjEsMzUuOWMxMi4xLDAuMiwyNC4yLDAuMSwzNi4yLDAuMWM0LjcsMC4yLDEwLjMtMi40LDExLTcuNgoJCWMwLjQtNi43LDAuMy0xMy40LDAuMS0yMC4xYy0wLjUtNS40LTYuMS04LjQtMTEuMS04LjNDMTQ1LjMsMTYuMywxMzMuMiwxNi4yLDEyMS4xLDE2LjV6Ii8+Cgk8cGF0aCBpZD0iWE1MSURfN18iIGNsYXNzPSJzdDEiIGQ9Ik04My41LDMzLjZjMC4xLTUuNyw0LjQtMTAuMyw5LjUtMTIuMmMyLjItMC4yLDQuNS0wLjIsNi43LDBjNS45LDIuMiwxMC40LDguMiw5LjQsMTQuNwoJCWMtMC40LDUuMy00LjYsOS4zLTkuNCwxMS4yYy0yLjIsMC4yLTQuNSwwLjItNi43LDBDODcuNCw0NS40LDgyLjgsMzkuOSw4My41LDMzLjZ6Ii8+CjwvZz4KPC9zdmc+Cg==">
                    </a>


                    <!-- close -->
                    <a class="sid-nav-cls" href="javascript:void(0);"><svg class="snv_cn-icn vj_icn vj_close">
                         <use xlink:href="#vj_close"></use>
                         </svg></a>

                    <a class="ndtv_logo" href="https://www.ndtv.com"> <svg focusable="false"
                         xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                         <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"></path>
                         </svg> Back to NDTV.com</a>
               </div>

               <div class="sid-nav_wrp pt0">
                    
                    <ul class="sid-nav_ul">
                         
                         <li class="snv-two">
                         <div class="sid-nav_li sid-nav_li-ttl">Our Tools </div>
                         <ul class="snv_cn-ul">
                         <li class="snv_cn-li"><a href="https://www.ndtv.com/traffic-challan" class="snv_cn-lnk ripple">
                              <div class="snv_ic-wrp">
                              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 581.8 980" class="vj_icn vj_shopping-icon"><path d="M581.8,355.1h-99.2v-52.4c46.1-35,81.3-82,99.2-136.2h-99.2v-36.4C482.6,58.2,424.3,0,352.6,0h-123.5C157.3,0,99.2,58.2,99.2,130.1v36.4H0c17.9,54.2,53,101.2,99.2,136.2v52.4H0c17.9,54.2,53,101.2,99.2,136.2v52.4H0c17.9,54.2,52.9,101.3,99.2,136.3v107.9c0,71.8,58.2,130.1,129.9,130.1h20.7v62h82.1v-62.1h20.7c71.8,0,130-58.3,130-130.1v-107.8c46.1-35,81.3-82.1,99.2-136.2h-99.2v-52.5c46.2-35,81.3-82,99.2-136.2Zm-291,462.6c-52.6,0-95.4-42.8-95.4-95.4s42.8-95.5,95.4-95.5,95.4,42.8,95.4,95.5c0,52.6-42.6,95.4-95.4,95.4Zm0-263.3c-52.6,0-95.4-42.7-95.4-95.4s42.8-95.5,95.4-95.5,95.4,42.7,95.4,95.5c0,52.7-42.6,95.4-95.4,95.4Zm0-263.4c-52.6,0-95.4-42.6-95.4-95.4s42.8-95.3,95.4-95.3,95.4,42.7,95.4,95.3c0,52.8-42.6,95.4-95.4,95.4Z"></path></svg></div>Challans</a></li>

                         <li class="snv_cn-li"><a href="https://www.ndtv.com/fuel-prices" class="snv_cn-lnk ripple">
                              <div class="snv_ic-wrp">
                                                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 893 980" class="vj_icn vj_shopping-icon"><path d="M578.5,962.8l6.9-8.9,.8-142.7c.3-78.4,1.3-142.4,2-142.4,4.3,0,18.4,7.9,22.7,12.8,4.8,5.4,5.1,10.2,6.4,96.7,1.3,90.1,1.3,91.1,7.9,109.3,15.8,42.9,50.5,75,93.4,86.3,18.9,4.8,54.4,4.8,73.5,0,48-12.5,88.1-54.4,98-102.9,2-9.3,2.8-113.5,2.8-342.2V185.8l-73.3-75c-40.6-41.3-77.3-76.8-82.2-79.1-11.5-5.4-30.1-3.6-40.8,3.8-11,7.9-16.6,19.7-16.3,34.2,.2,15.8,5.6,23.2,42.9,60.5,28.8,28.8,29.3,29.3,29.3,40.8,0,34.5,22.7,77.9,49.8,94.4l8.9,5.6V854.1l-6.4,13c-9.7,19.1-22.7,27.3-46,28.3-14.8,.8-20.4,0-28.6-4.1-13-6.9-25.3-20.7-28.6-32.9-1.8-5.8-2.8-41.6-2.8-90.2v-1.5c0-86.8-1-95.2-13.3-119.7-13-25.3-48.5-51.8-74.8-56.1-5.6-.8-13.3-2.3-17.1-2.8l-7.2-1.5-.5-280-.8-280.3-7.4-9.4c-12-15.9,0-16.8-200.7-16.9h-13.9c-21.3,0-44.8,0-70.8,0C81.3,.3,30,.8,23.8,3.6,13.4,8.2,2.6,21.2,.9,31.4,.3,34.7,0,147.2,0,305.6v26.4c0,51.4,0,107.1,0,165l.8,457.4,5.4,6.9c2.8,3.8,8.4,9.5,12.3,12.3,6.9,5.4,8.9,5.4,271.1,6.1,294.6,.8,274.6,1.8,288.9-16.8Zm-111.8-656.5H117v-91.4c0-50.3,.8-92.4,1.8-93.2,.8-1,78.1-1.8,172-1.8h175.9v93.2h0v93.2Zm280,24.5c1.3-10.7,0-15.1-14.3-43.4-8.7-17.4-17.1-32.9-18.9-34.2-2.5-2-6.1,2.3-15.1,18.1-23.2,40.8-27.6,58.7-17.4,75,16.8,28.1,62,17.4,65.6-15.6ZM119,490.1c0-32.9,32.4-52.1,62-36.8,24,12.2,28.6,46.7,8.9,66.4-26.8,26.8-71,8.4-71-29.6Zm132-5.9c6.1-29.9,37.8-43.9,63.8-28.6,31.7,18.4,23,69.9-12.8,76.8-28.6,5.4-56.7-21.2-51.1-48.2Z"></path></svg>

                              </div> Petrol/Diesel</a></li>
                                                  
                         <li class="snv_cn-li"><a href="https://www.ndtv.com/tools/pincodes" class="snv_cn-lnk ripple">
                                   <div class="snv_ic-wrp">
                                        <svg id="Layer_1" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 50.62 50.62" class="vj_icn vj_shopping-icon">
                                             <defs>
                                             <style>
                                                  .cls-1 {
                                                  fill: #333;
                                                  }
                                             </style>
                                             </defs>
                                             <path id="Page-1" class="cls-1" d="M37.55,19.39c.85-1.8,1.32-3.76,1.39-5.75,0-3.62-1.43-7.09-3.99-9.64-1.27-1.27-2.77-2.28-4.42-2.97-4.21-1.74-9.01-1.26-12.8,1.27-3.79,2.53-6.06,6.79-6.06,11.35,.07,1.99,.55,3.94,1.4,5.74H0v31.23H50.62V19.39h-13.07Zm-1.76,16.84l9.73-5.92c.49-.29,.95-.63,1.38-1v15.62l-11.11-8.7ZM25.31,3.72c5.47,.02,9.9,4.45,9.91,9.92,0,2.85-1.87,6.56-5.41,10.74-1.4,1.65-2.91,3.21-4.5,4.68-1.58-1.46-3.07-3.01-4.47-4.64-3.56-4.2-5.44-7.92-5.44-10.78,.02-5.47,4.44-9.9,9.91-9.92ZM15.19,23.1c2.54,3.66,5.54,6.98,8.93,9.87l1.19,.99,1.19-.99c3.39-2.89,6.39-6.21,8.93-9.87h11.21c-.47,1.68-1.56,3.12-3.05,4.04l-18.28,11.11L7.03,27.14c-1.49-.92-2.58-2.36-3.05-4.04H15.19ZM3.72,29.32c.43,.37,.89,.71,1.38,1l9.55,5.81L3.72,44.9v-15.58Zm3.43,17.6l10.88-8.73,7.28,4.43,7.09-4.32,10.97,8.62H7.15ZM25.31,6.34c-2.41,0-4.59,1.45-5.52,3.69-.92,2.23-.41,4.8,1.29,6.51,1.71,1.71,4.28,2.22,6.51,1.29,2.23-.92,3.69-3.1,3.69-5.52,0-3.3-2.67-5.97-5.97-5.97Zm0,8.22c-1.24,0-2.25-1.01-2.25-2.25s1.01-2.25,2.25-2.25,2.25,1.01,2.25,2.25c0,1.24-1.01,2.25-2.25,2.25Z"/>
                                        </svg>

                                   </div> Pin Code</a></li>
                         
                         <li class="snv_cn-li"><a href="https://www.ndtv.com/tools/calculator" class="snv_cn-lnk ripple">
                              <div class="snv_ic-wrp">
                              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 784 980" class="vj_icn vj_shopping-icon"><path d="M718,0H66C29.6,0,0,29.4,0,65.5V914.5c0,36,29.6,65.5,66,65.5H718c36.4,0,66-29.4,66-65.5V65.5c0-36.1-29.6-65.5-66-65.5ZM188,879.2c-32.9,0-59.5-26.5-59.5-59s26.6-59,59.5-59,59.5,26.4,59.5,59-26.6,59-59.5,59Zm0-203c-32.9,0-59.5-26.5-59.5-59.1s26.6-59,59.5-59,59.5,26.5,59.5,59-26.6,59.1-59.5,59.1Zm0-203c-32.9,0-59.5-26.5-59.5-59.1s26.6-59,59.5-59,59.5,26.4,59.5,59-26.6,59.1-59.5,59.1Zm204.5,406c-32.8,0-59.5-26.5-59.5-59s26.7-59,59.5-59,59.5,26.4,59.5,59-26.6,59-59.5,59Zm0-203c-32.8,0-59.5-26.5-59.5-59.1s26.7-59,59.5-59,59.5,26.5,59.5,59-26.6,59.1-59.5,59.1Zm0-203c-32.8,0-59.5-26.5-59.5-59.1s26.7-59,59.5-59,59.5,26.4,59.5,59-26.6,59.1-59.5,59.1Zm264.1,347c0,32.5-26.6,59-59.4,59s-59.5-26.5-59.5-59v-203.1c0-32.5,26.7-59,59.5-59s59.4,26.5,59.4,59v203.1Zm-59.5-347c-32.8,0-59.5-26.5-59.5-59.1s26.7-59,59.5-59,59.4,26.4,59.4,59c0,32.6-26.6,59.1-59.4,59.1Zm76.9-233c0,16.8-13.7,30.4-30.6,30.4H143.9c-16.9,0-30.6-13.6-30.6-30.4v-94.8c0-16.8,13.7-30.4,30.6-30.4h499.5c16.9,0,30.6,13.6,30.6,30.4v94.8Z"></path></svg></div> Calculators</a>
                         <ul class="global-nav_list">
                                        <li class="global-nav_item"><a href="https://www.ndtv.com/tools/calculator/home-loan-calculator-online">Home Loan Calculator</a></li>
                                        <li class="global-nav_item"><a href="https://www.ndtv.com/tools/calculator/personal-loan-calculator-online">Personal Loan Calculator</a></li>
                                        <li class="global-nav_item"><a href="https://www.ndtv.com/tools/calculator/car-loan-calculator-online">Car Loan Calculator</a></li>
                                        <li class="global-nav_item"><a href="https://www.ndtv.com/tools/calculator/age-calculator-online">Age Calculator</a></li>
                                        <li class="global-nav_item"><a href="https://www.ndtv.com/tools/calculator/ppf-calculator-online">PPF Calculator</a></li>
                                        <li class="global-nav_item"><a href="https://www.ndtv.com/tools/calculator/bmi-calculator-online">BMI Calculator</a></li>
                                        <li class="global-nav_item"><a href="https://www.ndtv.com/tools/calculator/fuel-cost-calculator-online">Fuel Cost Calculator</a></li>
                                        <li class="global-nav_item"><a href="https://www.ndtv.com/tools/calculator/sip-calculator-online">SIP Calculator</a></li>
                                        <li class="global-nav_item"><a href="https://www.ndtv.com/tools/calculator/date-calculator-online">Date Calculator</a></li>
                                                                           <li class="global-nav_item"><a href="https://www.ndtv.com/tools/calculator/percentage-calculator-online">Percentage Calculator</a></li>
                                                                           
                         </ul>
                         </li>
                         </ul>
                         </li>
                                   
                                   <li class="snv-two">
                                        <div class="sid-nav_li sid-nav_li-ttl">Follow Us On</div>
                                        <ul class="snv_cn-ul">
                                             <li class="snv_cn-li">
                                             <a class="snv_cn-lnk ripple" href="https://www.facebook.com/ndtv"
                                                  target="_blank">
                                                  <div class="snv_ic-wrp">
                                                       <svg class="vj_icn vj_auto">
                                                            <use xlink:href="#vj_facebook"></use>
                                                       </svg>
                                                  </div> Facebook
                                             </a>
                                             </li>
                                             <li class="snv_cn-li">
                                             <a class="snv_cn-lnk ripple" href="https://twitter.com/ndtv"
                                                  target="_blank">
                                                  <div class="snv_ic-wrp">
                                                       <svg class="vj_icn vj_world-web">
                                                            <use xlink:href="#vj_twitter"></use>
                                                       </svg>
                                                  </div> Twitter
                                             </a>
                                             </li>


                                             <li class="snv_cn-li">
                                             <a class="snv_cn-lnk ripple" href="https://www.instagram.com/ndtv/?hl=en"
                                                  target="_blank">
                                                  <div class="snv_ic-wrp">
                                                       <svg class="vj_icn vj_cities">
                                                            <use xlink:href="#insta"></use>
                                                       </svg>
                                                  </div> Instagram
                                             </a>
                                             </li>


                                             <li class="snv_cn-li">
                                             <a class="snv_cn-lnk ripple" href="https://www.linkedin.com/company/ndtv"
                                                  target="_blank">
                                                  <div class="snv_ic-wrp">
                                                       <svg class="vj_icn vj_cities">
                                                            <use xlink:href="#linkedin"></use>
                                                       </svg>
                                                  </div> Linkedin
                                             </a>
                                             </li>
                                             <li class="snv_cn-li">
                                             <a class="snv_cn-lnk ripple" href="https://www.youtube.com/user/ndtv">
                                                  <div class="snv_ic-wrp">
                                                       <svg class="vj_icn vj_south">
                                                            <use xlink:href="#youtube"></use>
                                                       </svg>
                                                  </div> Youtube
                                             </a>
                                             </li>


                                             <li class="snv_cn-li">
                                             <a class="snv_cn-lnk ripple" href="https://www.kooapp.com/profile/ndtv"
                                                  target="_blank">
                                                  <div class="snv_ic-wrp">

                                                       <svg class="vj_icn vj_opinion">
                                                            <use xlink:href="#koos"></use>
                                                       </svg>

                                                  </div> Koo
                                             </a>
                                             </li>
                                        </ul>
                                   </li>
                              </ul>
                         </div>
                         </li>
                    </ul>
               </div>
          </div>
     </div>

     <!--======[ NDTV WAP Slide Navigation SVG Icons start ]======-->
     <svg aria-hidden="true" style="position: absolute; width: 0; height: 0; overflow: hidden;" version="1.1"
          xmlns="https://www.w3.org/2000/svg" xmlns:xlink="https://www.w3.org/1999/xlink">
          <defs>
               <!-- vj_home -->
               <symbol id="vj_home" viewBox="0 0 32 32">
                    <path
                         d="M29.504 10.988l-12.469-8.906c-0.288-0.207-0.647-0.331-1.035-0.331s-0.748 0.124-1.040 0.335l0.005-0.004-12.469 8.906c-0.454 0.327-0.746 0.854-0.746 1.449v0 16.031c0 0 0 0.001 0 0.001 0 0.983 0.797 1.78 1.78 1.78 0 0 0.001 0 0.001 0h24.937c0 0 0.001 0 0.001 0 0.983 0 1.78-0.797 1.78-1.78 0-0 0-0.001 0-0.001v0-16.031c0-0.595-0.292-1.122-0.741-1.445l-0.005-0.004zM14.219 26.687v-7.125h3.563v7.125zM26.688 26.687h-5.344v-8.906c0-0 0-0.001 0-0.001 0-0.983-0.797-1.78-1.78-1.78-0 0-0.001 0-0.001 0h-7.125c-0 0-0.001 0-0.001 0-0.983 0-1.78 0.797-1.78 1.78 0 0 0 0.001 0 0.001v-0 8.906h-5.344v-13.333l10.688-7.635 10.688 7.635z">
                    </path>
               </symbol>
               <!-- HOP Logo -->
               <symbol id="vj_hop-icon" viewBox="0 0 32 32">
                    <path
                         d="M9.222 18.918c-0.365-0.845-0.602-1.811-0.602-2.778s0.243-1.933 0.602-2.778c0.365-0.845 0.845-1.69 1.568-2.291 0.48-0.48 0.966-0.845 1.446-1.088v-0.602h-3.501v4.947h-5.19v-4.947h-3.494v13.638h3.501v-5.427h5.069v5.312h3.501v-0.602c-0.602-0.365-1.088-0.723-1.446-1.088-0.608-0.608-1.094-1.453-1.453-2.298z">
                    </path>
                    <path
                         d="M18.272 13.485c-0.365-0.365-0.723-0.602-1.21-0.845-0.48-0.243-0.966-0.243-1.446-0.243s-0.966 0.122-1.446 0.243c-0.48 0.243-0.845 0.48-1.21 0.845s-0.602 0.723-0.845 1.21c-0.243 0.48-0.365 0.966-0.365 1.568s0.122 1.088 0.365 1.568 0.48 0.845 0.845 1.21c0.365 0.365 0.723 0.602 1.21 0.845s0.966 0.243 1.446 0.243 0.966-0.122 1.446-0.243c0.48-0.243 0.845-0.48 1.21-0.845s0.602-0.723 0.845-1.21c0.243-0.48 0.365-0.966 0.365-1.568s-0.122-1.088-0.365-1.568c-0.243-0.486-0.486-0.845-0.845-1.21z">
                    </path>
                    <path
                         d="M30.938 10.349c-0.845-0.845-1.933-1.21-3.501-1.21h-5.67v13.638h3.501v-4.467h2.054c1.568 0 2.656-0.365 3.501-1.21s1.21-1.933 1.21-3.379c0.115-1.44-0.25-2.528-1.094-3.373zM26.477 15.418h-1.21v-3.379h1.21c1.325 0 1.933 0.602 1.933 1.69s-0.608 1.69-1.933 1.69z">
                    </path>
               </symbol>
               <!-- vj_coronavirus -->
               <symbol id="vj_coronavirus" viewBox="0 0 32 32">
                    <path
                         d="M28.587 11.973c-0.817 0-1.605 0.322-2.189 0.895h-0.596c-0.173-0.549-0.394-1.080-0.656-1.587l0.418-0.418c0.817-0.012 1.605-0.34 2.177-0.913 1.223-1.223 1.223-3.209 0-4.426l-1.265-1.265c-1.223-1.223-3.209-1.223-4.426 0-0.579 0.579-0.907 1.36-0.913 2.177l-0.418 0.418c-0.507-0.262-1.038-0.483-1.587-0.656v-0.596c0.573-0.585 0.895-1.372 0.895-2.189 0-1.724-1.408-3.132-3.132-3.132h-1.79c-1.724 0-3.132 1.408-3.132 3.132 0 0.817 0.322 1.605 0.895 2.189v0.596c-0.543 0.173-1.080 0.394-1.587 0.656l-0.418-0.418c-0.012-0.817-0.334-1.605-0.913-2.177-1.223-1.223-3.209-1.223-4.426 0l-1.271 1.259c-0.591 0.591-0.913 1.378-0.913 2.213s0.322 1.623 0.913 2.213c0.579 0.579 1.36 0.907 2.177 0.913l0.418 0.418c-0.262 0.507-0.483 1.038-0.656 1.587h-0.596c-0.585-0.573-1.372-0.895-2.189-0.895-1.724 0-3.132 1.408-3.132 3.132v1.79c0 1.724 1.408 3.132 3.132 3.132 0.817 0 1.605-0.322 2.189-0.895h0.596c0.173 0.549 0.394 1.080 0.656 1.587l-0.418 0.418c-0.817 0.012-1.605 0.34-2.177 0.913-0.591 0.591-0.919 1.378-0.919 2.213s0.328 1.623 0.919 2.213l1.265 1.265c1.223 1.223 3.209 1.223 4.426 0 0.579-0.579 0.907-1.36 0.913-2.177l0.418-0.418c0.507 0.262 1.038 0.483 1.587 0.656v0.596c-0.573 0.585-0.895 1.372-0.895 2.189 0 1.724 1.408 3.132 3.132 3.132h1.79c1.724 0 3.132-1.408 3.132-3.132 0-0.817-0.322-1.605-0.895-2.189v-0.596c0.543-0.173 1.080-0.394 1.587-0.656l0.418 0.418c0.012 0.817 0.334 1.605 0.913 2.177 0.608 0.608 1.414 0.919 2.213 0.919s1.605-0.304 2.213-0.919l1.265-1.265c0.591-0.591 0.913-1.378 0.913-2.213s-0.322-1.623-0.913-2.213c-0.579-0.579-1.36-0.907-2.177-0.913l-0.418-0.418c0.262-0.507 0.483-1.038 0.656-1.587h0.596c0.585 0.573 1.372 0.895 2.189 0.895 1.724 0 3.132-1.408 3.132-3.132v-1.79c0.006-1.718-1.402-3.126-3.126-3.126zM23.451 17.521c-0.197 0.954-0.567 1.855-1.11 2.672-0.352 0.531-0.28 1.241 0.167 1.688l1.605 1.605c0.334 0.334 0.829 0.471 1.294 0.346 0.155-0.042 0.322 0 0.435 0.113 0.084 0.084 0.131 0.197 0.131 0.316s-0.048 0.233-0.131 0.316l-1.265 1.265c-0.173 0.173-0.459 0.173-0.632 0-0.113-0.113-0.155-0.28-0.113-0.435 0.119-0.459-0.012-0.954-0.346-1.294l-1.605-1.605c-0.447-0.447-1.157-0.519-1.688-0.167-0.817 0.543-1.712 0.913-2.672 1.11-0.62 0.125-1.074 0.68-1.074 1.312v2.267c0 0.477 0.256 0.919 0.668 1.157 0.143 0.084 0.227 0.233 0.227 0.388 0 0.245-0.203 0.447-0.447 0.447h-1.79c-0.245 0-0.447-0.203-0.447-0.447 0-0.155 0.089-0.304 0.227-0.388 0.412-0.239 0.668-0.686 0.668-1.157v-2.267c0-0.638-0.453-1.187-1.074-1.312-0.954-0.197-1.855-0.567-2.672-1.11-0.221-0.143-0.477-0.221-0.74-0.221-0.358 0-0.698 0.137-0.948 0.394l-1.605 1.605c-0.334 0.334-0.471 0.829-0.346 1.294 0.042 0.155 0 0.322-0.113 0.435-0.083 0.084-0.197 0.131-0.316 0.131s-0.233-0.048-0.316-0.131l-1.265-1.265c-0.083-0.084-0.131-0.191-0.131-0.316 0-0.119 0.048-0.233 0.131-0.316 0.113-0.113 0.28-0.155 0.435-0.113 0.459 0.119 0.954-0.012 1.294-0.346l1.605-1.605c0.447-0.447 0.519-1.163 0.167-1.688-0.543-0.817-0.913-1.712-1.11-2.672-0.125-0.62-0.68-1.074-1.312-1.074h-2.273c-0.477 0-0.919 0.256-1.157 0.668-0.083 0.143-0.233 0.227-0.388 0.227-0.245 0-0.447-0.203-0.447-0.447v-1.79c0-0.245 0.203-0.447 0.447-0.447 0.155 0 0.304 0.089 0.388 0.227 0.239 0.412 0.686 0.668 1.157 0.668h2.267c0.638 0 1.187-0.453 1.318-1.074 0.197-0.954 0.567-1.855 1.11-2.672 0.352-0.531 0.28-1.241-0.167-1.688l-1.605-1.605c-0.334-0.334-0.829-0.471-1.294-0.346-0.155 0.042-0.322 0-0.435-0.113-0.083-0.083-0.131-0.197-0.131-0.316s0.048-0.233 0.131-0.316l1.265-1.265c0.173-0.173 0.459-0.173 0.632 0 0.113 0.113 0.155 0.28 0.113 0.435-0.119 0.459 0.012 0.954 0.346 1.294l1.605 1.605c0.447 0.447 1.163 0.519 1.688 0.167 0.817-0.543 1.712-0.913 2.672-1.11 0.62-0.125 1.074-0.68 1.074-1.318v-2.273c0-0.477-0.256-0.919-0.668-1.157-0.143-0.083-0.227-0.233-0.227-0.388 0-0.245 0.203-0.447 0.447-0.447h1.79c0.245 0 0.447 0.203 0.447 0.447 0 0.155-0.089 0.304-0.227 0.388-0.412 0.239-0.668 0.686-0.668 1.157v2.267c0 0.638 0.453 1.187 1.074 1.318 0.954 0.197 1.855 0.567 2.672 1.11 0.531 0.352 1.241 0.28 1.688-0.167l1.605-1.605c0.334-0.334 0.471-0.829 0.346-1.294-0.042-0.155 0-0.322 0.113-0.435 0.084-0.083 0.197-0.131 0.316-0.131s0.233 0.048 0.316 0.131l1.265 1.265c0.084 0.083 0.131 0.191 0.131 0.316 0 0.119-0.048 0.233-0.131 0.316-0.113 0.113-0.28 0.155-0.435 0.113-0.459-0.119-0.954 0.012-1.294 0.346l-1.605 1.605c-0.447 0.447-0.519 1.157-0.167 1.688 0.543 0.817 0.913 1.712 1.11 2.672 0.125 0.62 0.68 1.074 1.318 1.074h2.267c0.477 0 0.919-0.256 1.163-0.668 0.084-0.143 0.233-0.227 0.388-0.227 0.245 0 0.447 0.203 0.447 0.447v1.79c0 0.245-0.203 0.447-0.447 0.447-0.155 0-0.304-0.089-0.388-0.227-0.239-0.412-0.686-0.668-1.157-0.668h-2.267c-0.644 0-1.193 0.453-1.324 1.074z">
                    </path>
                    <path
                         d="M22.323 16c0 0.494-0.401 0.895-0.895 0.895s-0.895-0.401-0.895-0.895c0-0.494 0.401-0.895 0.895-0.895s0.895 0.401 0.895 0.895z">
                    </path>
                    <path
                         d="M16.474 20.661c0.42 0.26 0.551 0.811 0.291 1.232s-0.811 0.551-1.232 0.291c-0.42-0.26-0.551-0.811-0.291-1.232s0.811-0.551 1.231-0.291z">
                    </path>
                    <path
                         d="M11.466 16c0 0.494-0.401 0.895-0.895 0.895s-0.895-0.401-0.895-0.895c0-0.494 0.401-0.895 0.895-0.895s0.895 0.401 0.895 0.895z">
                    </path>
                    <path
                         d="M16.308 9.737c0.463 0.173 0.698 0.688 0.525 1.151s-0.688 0.698-1.151 0.525c-0.463-0.173-0.698-0.688-0.525-1.151s0.688-0.698 1.151-0.525z">
                    </path>
                    <path
                         d="M20.73 19.836c0 0.494-0.401 0.895-0.895 0.895s-0.895-0.401-0.895-0.895c0-0.494 0.401-0.895 0.895-0.895s0.895 0.401 0.895 0.895z">
                    </path>
                    <path
                         d="M13.059 19.836c0 0.494-0.401 0.895-0.895 0.895s-0.895-0.401-0.895-0.895c0-0.494 0.401-0.895 0.895-0.895s0.895 0.401 0.895 0.895z">
                    </path>
                    <path
                         d="M13.059 12.164c0 0.494-0.401 0.895-0.895 0.895s-0.895-0.401-0.895-0.895c0-0.494 0.401-0.895 0.895-0.895s0.895 0.401 0.895 0.895z">
                    </path>
                    <path
                         d="M20.73 12.164c0 0.494-0.401 0.895-0.895 0.895s-0.895-0.401-0.895-0.895c0-0.494 0.401-0.895 0.895-0.895s0.895 0.401 0.895 0.895z">
                    </path>
                    <path
                         d="M16.895 13.614c0 0.494-0.401 0.895-0.895 0.895s-0.895-0.401-0.895-0.895c0-0.494 0.401-0.895 0.895-0.895s0.895 0.401 0.895 0.895z">
                    </path>
                    <path
                         d="M16.895 18.386c0 0.494-0.401 0.895-0.895 0.895s-0.895-0.401-0.895-0.895c0-0.494 0.401-0.895 0.895-0.895s0.895 0.401 0.895 0.895z">
                    </path>
                    <path
                         d="M19.211 15.639c0.19 0.456-0.026 0.98-0.482 1.17s-0.98-0.026-1.17-0.482c-0.19-0.456 0.026-0.98 0.482-1.17s0.98 0.026 1.17 0.482z">
                    </path>
                    <path
                         d="M14.519 15.947c0.026 0.494-0.353 0.915-0.846 0.941s-0.915-0.353-0.941-0.846c-0.026-0.493 0.353-0.915 0.846-0.941s0.915 0.353 0.941 0.846z">
                    </path>
               </symbol>
               <!-- vj_live-tv -->
               <symbol id="vj_live-tv" viewBox="0 0 32 32">
                    <path
                         d="M26.99 19.55c0 1.052-0.852 1.904-1.904 1.904s-1.904-0.852-1.904-1.904c0-1.052 0.852-1.904 1.904-1.904s1.904 0.852 1.904 1.904z">
                    </path>
                    <path
                         d="M20.813 11.886c-0.711 0-1.287 0.552-1.287 1.587v11.989c0 1.034 0.576 1.587 1.287 1.587s1.287-0.552 1.287-1.587v-11.989c0-1.034-0.576-1.587-1.287-1.587z">
                    </path>
                    <path
                         d="M26.99 15.083c0 1.052-0.852 1.904-1.904 1.904s-1.904-0.852-1.904-1.904c0-1.052 0.852-1.904 1.904-1.904s1.904 0.852 1.904 1.904z">
                    </path>
                    <path
                         d="M23.993 7.185h-6.576c0.594-0.206 1.134-0.546 1.593-1.005l0.012-0.012 2.674-2.721c0.729-0.74 0.717-1.933-0.023-2.662-0.353-0.347-0.823-0.541-1.316-0.541-0.006 0-0.012 0-0.018 0-0.5 0.006-0.976 0.206-1.322 0.564l-2.662 2.715c-0.088 0.088-0.2 0.129-0.323 0.129s-0.235-0.047-0.323-0.135l-2.721-2.715c-0.735-0.735-1.928-0.735-2.662-0.006-0.735 0.735-0.735 1.928-0.006 2.662l2.715 2.721c0.458 0.458 0.999 0.799 1.593 1.005h-6.617c-4.278 0-7.758 3.479-7.758 7.758v9.050c0 4.278 3.479 7.758 7.758 7.758h15.985c4.278 0 7.758-3.479 7.758-7.758v-9.050c0-4.278-3.479-7.758-7.758-7.758zM23.993 27.989h-15.985c-2.204 0-3.996-1.793-3.996-3.996v-9.050c0-2.204 1.793-3.996 3.996-3.996h15.985c2.204 0 3.996 1.793 3.996 3.996v9.050c0 2.204-1.793 3.996-3.996 3.996zM18.509 5.68v0 0 0z">
                    </path>
               </symbol>
               <!-- vj_india -->
               <symbol id="vj_india" viewBox="0 0 32 32">
                    <path
                         d="M16 0c-8.822 0-16 7.178-16 16s7.178 16 16 16 16-7.178 16-16-7.178-16-16-16v0zM26.256 10.416c0.616 0 1.178 0.403 1.438 1.025 0.191 0.459 0.178 0.981-0.034 1.391-0.209 0.409-0.603 0.688-1.137 0.809-0.887 0.203-4.322 0.925-6.831 1.45-0.462 0.097-0.909 0.159-1.234 0.178 0.209-0.188 0.544-0.45 1-0.75 1.472-0.963 4.988-3.259 5.853-3.803 0.316-0.2 0.634-0.3 0.947-0.3v0zM23.772 6.828c0.428 0 0.856 0.184 1.175 0.506 0.353 0.353 0.538 0.838 0.5 1.297-0.038 0.456-0.294 0.866-0.741 1.184-0.725 0.516-3.528 2.434-5.756 3.953-0.45 0.309-0.822 0.516-1.075 0.637 0.122-0.253 0.328-0.625 0.637-1.075 1.519-2.225 3.438-5.028 3.956-5.756 0.347-0.487 0.797-0.747 1.303-0.747v0zM20.172 4.459c0.228 0 0.459 0.047 0.672 0.134 0.459 0.191 0.819 0.566 0.959 1.006 0.141 0.438 0.059 0.912-0.231 1.375-0.472 0.753-2.331 3.6-3.803 5.853-0.297 0.456-0.559 0.791-0.747 0.997 0.012-0.281 0.066-0.703 0.178-1.234 0.359-1.722 1.222-5.838 1.45-6.828 0.181-0.816 0.75-1.303 1.522-1.303v0zM17.353 16.284c0 0.747-0.606 1.353-1.353 1.353s-1.353-0.606-1.353-1.353c0-0.747 0.606-1.353 1.353-1.353s1.353 0.606 1.353 1.353zM14.728 4.191c0.297-0.353 0.772-0.563 1.272-0.563 0.497 0 0.972 0.209 1.272 0.563 0.297 0.35 0.403 0.822 0.313 1.359-0.159 0.941-0.866 4.703-1.275 6.866-0.119 0.622-0.231 1.091-0.309 1.359-0.078-0.269-0.191-0.738-0.309-1.359-0.409-2.162-1.116-5.931-1.275-6.866-0.091-0.537 0.016-1.009 0.313-1.359v0zM10.197 5.597c0.141-0.441 0.5-0.816 0.959-1.006 0.213-0.088 0.444-0.134 0.672-0.134 0.769 0 1.341 0.487 1.525 1.306 0.225 0.984 1.091 5.103 1.45 6.828 0.113 0.534 0.162 0.956 0.178 1.234-0.188-0.209-0.45-0.541-0.75-0.997-1.475-2.256-3.331-5.103-3.803-5.853-0.291-0.463-0.369-0.941-0.231-1.378v0zM7.050 7.334c0.322-0.322 0.75-0.506 1.175-0.506 0.506 0 0.956 0.256 1.303 0.747 0.406 0.572 1.734 2.506 3.953 5.753 0.306 0.45 0.516 0.822 0.634 1.075-0.253-0.122-0.622-0.328-1.072-0.634-3.25-2.216-5.184-3.547-5.756-3.953-0.447-0.316-0.703-0.725-0.741-1.181-0.034-0.463 0.153-0.947 0.503-1.3v0zM4.306 11.441c0.259-0.622 0.822-1.025 1.438-1.025 0.313 0 0.631 0.1 0.944 0.297 0.594 0.372 2.506 1.616 5.853 3.803 0.456 0.297 0.791 0.559 1 0.747-0.328-0.016-0.775-0.081-1.238-0.178-3.925-0.822-6.159-1.297-6.828-1.45-0.534-0.122-0.925-0.403-1.138-0.809-0.209-0.406-0.222-0.925-0.031-1.384v0zM3.344 16.284c0-0.803 0.534-1.616 1.559-1.616 0.116 0 0.237 0.009 0.362 0.031 0.875 0.147 4.216 0.775 6.863 1.275 0.622 0.119 1.091 0.231 1.359 0.309-0.272 0.078-0.738 0.191-1.359 0.309-2.65 0.5-5.991 1.128-6.862 1.275-1.253 0.212-1.922-0.691-1.922-1.584v0zM4.306 21.128c-0.191-0.459-0.178-0.978 0.034-1.391 0.209-0.409 0.603-0.688 1.138-0.809 0.925-0.212 4.675-1 6.828-1.45 0.463-0.097 0.909-0.159 1.238-0.178-0.209 0.188-0.544 0.45-1 0.75-3.297 2.156-5.266 3.438-5.853 3.806-0.938 0.587-1.994 0.209-2.384-0.728v0zM8.228 25.741c-0.428 0-0.856-0.184-1.175-0.506-0.353-0.353-0.537-0.837-0.5-1.297 0.037-0.456 0.294-0.866 0.741-1.184 0.572-0.406 2.506-1.734 5.753-3.953 0.45-0.306 0.822-0.516 1.075-0.634-0.122 0.253-0.328 0.622-0.634 1.072-2.219 3.25-3.55 5.188-3.956 5.756-0.347 0.488-0.797 0.747-1.303 0.747v0zM11.828 28.109c-0.228 0-0.459-0.047-0.672-0.134-0.459-0.191-0.819-0.566-0.959-1.006-0.137-0.438-0.059-0.913 0.231-1.375 0.369-0.591 1.65-2.559 3.803-5.853 0.297-0.456 0.559-0.791 0.747-0.997-0.016 0.281-0.066 0.703-0.178 1.234-0.359 1.722-1.222 5.838-1.45 6.828-0.181 0.816-0.753 1.306-1.522 1.303v0zM17.272 28.378c-0.3 0.353-0.775 0.563-1.272 0.563s-0.972-0.209-1.272-0.563c-0.297-0.35-0.403-0.822-0.313-1.363 0.156-0.934 0.866-4.7 1.275-6.866 0.119-0.622 0.231-1.091 0.309-1.359 0.078 0.272 0.191 0.738 0.309 1.359 0.406 2.159 1.116 5.925 1.275 6.866 0.091 0.541-0.016 1.009-0.313 1.363v0zM21.803 26.969c-0.141 0.441-0.5 0.816-0.959 1.006-0.212 0.087-0.447 0.134-0.675 0.134-0.769 0-1.341-0.488-1.525-1.306-0.212-0.925-1-4.675-1.45-6.828-0.113-0.534-0.163-0.956-0.178-1.234 0.188 0.209 0.45 0.541 0.75 0.997 1.475 2.253 3.331 5.1 3.803 5.853 0.294 0.466 0.372 0.944 0.234 1.378v0zM24.95 25.234c-0.322 0.322-0.75 0.506-1.175 0.506-0.506 0-0.959-0.256-1.306-0.747-0.516-0.728-2.434-3.531-3.953-5.753-0.306-0.45-0.516-0.822-0.634-1.075 0.253 0.122 0.622 0.328 1.072 0.634 2.225 1.519 5.031 3.438 5.756 3.953 0.447 0.316 0.703 0.725 0.741 1.181 0.041 0.462-0.147 0.947-0.5 1.3v0zM27.694 21.128c-0.387 0.938-1.444 1.319-2.384 0.728-0.753-0.472-3.6-2.331-5.853-3.803-0.456-0.297-0.791-0.563-1-0.75 0.328 0.016 0.775 0.081 1.234 0.178 2.634 0.55 5.956 1.25 6.828 1.45 0.534 0.122 0.925 0.403 1.137 0.809 0.216 0.409 0.228 0.928 0.038 1.387v0zM26.734 17.869c-0.694-0.116-3.003-0.547-6.866-1.275-0.622-0.116-1.091-0.228-1.359-0.309 0.269-0.078 0.738-0.191 1.359-0.309 3.863-0.728 6.172-1.156 6.866-1.275 1.253-0.209 1.922 0.691 1.922 1.584s-0.669 1.797-1.922 1.584v0z">
                    </path>
               </symbol>
               <!-- vj_latest -->
               <symbol id="vj_latest" viewBox="0 0 32 32">
                    <path
                         d="M28.906 1.25h-18.438c-0 0-0.001 0-0.001 0-1.018 0-1.843 0.825-1.843 1.843 0 0 0 0.001 0 0.001v-0 5.531h-5.531c-0 0-0.001 0-0.001 0-1.018 0-1.843 0.825-1.843 1.843 0 0 0 0.001 0 0.001v-0 14.75c0.003 3.053 2.478 5.528 5.531 5.531h18.438c3.053-0.003 5.528-2.478 5.531-5.531v-22.125c0-0 0-0.001 0-0.001 0-1.018-0.825-1.843-1.843-1.843-0 0-0.001 0-0.001 0h0zM4.938 12.313h3.688v12.906c0 1.018-0.825 1.844-1.844 1.844s-1.844-0.825-1.844-1.844v0zM27.063 25.219c-0.002 1.017-0.826 1.842-1.844 1.844h-13.246c0.209-0.547 0.333-1.18 0.34-1.841l0-0.003v-20.281h14.75z">
                    </path>
                    <path
                         d="M17.844 12.313h3.688c1.018 0 1.844-0.825 1.844-1.844s-0.825-1.844-1.844-1.844v0h-3.688c-1.018 0-1.844 0.825-1.844 1.844s0.825 1.844 1.844 1.844v0z">
                    </path>
                    <path
                         d="M21.531 16h-3.688c-1.018 0-1.844 0.825-1.844 1.844s0.825 1.844 1.844 1.844v0h3.688c1.018 0 1.844-0.825 1.844-1.844s-0.825-1.844-1.844-1.844v0z">
                    </path>
               </symbol>
               <!-- vj_videos -->
               <symbol id="vj_videos" viewBox="0 0 32 32">
                    <path
                         d="M22.6 13.567v-2.433c0-2.2-1.8-4-4-4h-14.667c-2.2 0-4 1.8-4 4v10.667c0 2.2 1.8 4 4 4h14.667c2.2 0 4-1.8 4-4v-2.367l9.333 5.2v-16.167l-9.333 5.1zM18.6 20.467c0 0.733-0.6 1.333-1.333 1.333h-12c-0.733 0-1.333-0.6-1.333-1.333v-8c0-0.733 0.6-1.333 1.333-1.333h12c0.733 0 1.333 0.6 1.333 1.333v8zM27.933 18.767l-3.8-2.267 3.8-2.2v4.467z">
                    </path>
               </symbol>
               <!-- vj_cricket -->
               <symbol id="vj_cricket" viewBox="0 0 32 32">
                    <path
                         d="M13.772 3.638h0.881c0.484 0 0.878-0.394 0.878-0.878s-0.394-0.878-0.878-0.878h-0.881c-0.031-0.459-0.409-0.819-0.875-0.819s-0.847 0.363-0.875 0.819h-0.006c-0.031-0.459-0.409-0.819-0.875-0.819s-0.847 0.363-0.875 0.819h-0.881c-0.484 0-0.878 0.394-0.878 0.878s0.394 0.878 0.878 0.878h0.881c0.031 0.459 0.409 0.822 0.875 0.822s0.847-0.362 0.875-0.819h0.006c0.031 0.459 0.409 0.819 0.875 0.819s0.844-0.366 0.875-0.822z">
                    </path>
                    <path
                         d="M21.741 3.638h0.878c0.484 0 0.878-0.394 0.878-0.878s-0.394-0.878-0.878-0.878h-0.878c0-0.484-0.394-0.878-0.878-0.878s-0.878 0.394-0.878 0.878c0-0.484-0.394-0.878-0.878-0.878s-0.878 0.394-0.878 0.878h-0.878c-0.484 0-0.878 0.394-0.878 0.878s0.394 0.878 0.878 0.878h0.878c0 0.484 0.394 0.878 0.878 0.878s0.878-0.394 0.878-0.878c0 0.484 0.394 0.878 0.878 0.878s0.878-0.394 0.878-0.878z">
                    </path>
                    <path
                         d="M8.069 5.134c-1.125 0-2.041 0.916-2.041 2.041v21.516c0 0.181 0.072 0.353 0.2 0.481l1.362 1.363c0.266 0.266 0.697 0.266 0.963 0l1.363-1.363c0.128-0.128 0.2-0.3 0.2-0.481v-21.512c-0.003-1.125-0.922-2.044-2.047-2.044z">
                    </path>
                    <path
                         d="M16 5.134c-1.125 0-2.041 0.916-2.041 2.041v21.516c0 0.181 0.072 0.353 0.2 0.481l1.363 1.363c0.266 0.266 0.697 0.266 0.963 0l1.363-1.363c0.128-0.128 0.2-0.3 0.2-0.481v-21.512c-0.006-1.125-0.922-2.044-2.047-2.044v0z">
                    </path>
                    <path
                         d="M23.909 5.134c-1.125 0-2.041 0.916-2.041 2.041v21.516c0 0.181 0.072 0.353 0.2 0.481l1.363 1.363c0.266 0.266 0.697 0.266 0.962 0l1.363-1.363c0.128-0.128 0.2-0.3 0.2-0.481v-21.512c-0.003-1.125-0.919-2.044-2.047-2.044z">
                    </path>
               </symbol>
               <!-- vj_gadgets -->
               <symbol id="vj_gadgets" viewBox="0 0 32 32">
                    <path
                         d="M18.905 14.548h-1.452v-1.452c0-0.726-0.726-1.452-1.452-1.452s-1.452 0.726-1.452 1.452v2.905c0 0.726 0.726 1.452 1.452 1.452h2.905c0.726 0 1.452-0.726 1.452-1.452s-0.726-1.452-1.452-1.452z">
                    </path>
                    <path
                         d="M23.988 8.593v-2.76c0-2.905-2.179-5.083-5.083-5.083h-5.81c-2.905 0-5.083 2.179-5.083 5.083v2.76c-1.888 2.179-2.905 4.793-2.905 7.407s1.017 5.229 2.905 7.407v2.76c0 2.905 2.179 5.083 5.083 5.083h5.81c2.905 0 5.083-2.179 5.083-5.083v-2.76c1.888-2.179 2.905-4.793 2.905-7.407s-1.017-5.229-2.905-7.407zM22.536 16c0 3.631-2.905 6.536-6.536 6.536s-6.536-2.905-6.536-6.536 2.905-6.536 6.536-6.536 6.536 2.905 6.536 6.536zM19.631 7.286c-1.162-0.436-2.324-0.726-3.631-0.726s-2.469 0.29-3.631 0.726v-1.452c0-0.436 0.29-0.726 0.726-0.726h5.81c0.436 0 0.726 0.29 0.726 0.726v1.452zM12.369 24.714c2.324 1.017 4.938 1.017 7.262 0v1.452c0 0.436-0.29 0.726-0.726 0.726h-5.81c-0.436 0-0.726-0.29-0.726-0.726v-1.452z">
                    </path>
               </symbol>
               <!-- vj_movies -->
               <symbol id="vj_movies" viewBox="0 0 32 32">
                    <path
                         d="M1.635 18.144c0 6.936 5.625 12.561 12.561 12.561s12.561-5.625 12.561-12.561c0-2.371-1.017-5.386-1.838-6.666-0.711-1.097-0.956-1.801-0.956-2.831 0-2.145 2.261-4.289 4.633-4.289h0.306c0.845 0 1.532-0.686 1.532-1.532s-0.686-1.532-1.532-1.532h-0.306c-3.769 0-6.991 2.010-7.757 6.127-1.569-1.189-4.007-1.838-6.642-1.838-6.936-0-12.561 5.625-12.561 12.561zM12.664 18.144c0-0.845 0.686-1.532 1.532-1.532s1.532 0.686 1.532 1.532c0 0.846-0.686 1.532-1.532 1.532s-1.532-0.686-1.532-1.532zM4.698 18.144c0-1.526 1.231-2.757 2.757-2.757s2.757 1.231 2.757 2.757c0 1.526-1.231 2.757-2.757 2.757s-2.757-1.231-2.757-2.757zM18.178 18.144c0-1.526 1.231-2.757 2.757-2.757s2.757 1.231 2.757 2.757c0 1.526-1.232 2.757-2.757 2.757s-2.757-1.231-2.757-2.757zM11.438 24.885c0-1.526 1.231-2.758 2.757-2.758s2.757 1.232 2.757 2.758c0 1.526-1.231 2.757-2.757 2.757s-2.757-1.231-2.757-2.757zM11.438 11.405c0-1.526 1.231-2.757 2.757-2.757s2.757 1.231 2.757 2.757c0 1.526-1.231 2.757-2.757 2.757s-2.757-1.232-2.757-2.757z">
                    </path>
               </symbol>


               <!-- vj_amp-stories -->
               <symbol id="vj_amp-stories" viewBox="0 0 38 32">
                    <path d="M9.485 2h19.285v29h-19.285v-29z"></path>
                    <path d="M1.801 5.915h3.915v21.315h-3.915v-21.315z"></path>
                    <path d="M32.685 5.915h3.915v21.315h-3.915v-21.315z"></path>
               </symbol>
               <!-- vj_hop -->
               <symbol id="vj_hop" viewBox="0 0 32 32">
                    <path
                         d="M9.222 18.918c-0.365-0.845-0.602-1.811-0.602-2.778s0.243-1.933 0.602-2.778c0.365-0.845 0.845-1.69 1.568-2.291 0.48-0.48 0.966-0.845 1.446-1.088v-0.602h-3.501v4.947h-5.19v-4.947h-3.494v13.638h3.501v-5.427h5.069v5.312h3.501v-0.602c-0.602-0.365-1.088-0.723-1.446-1.088-0.608-0.608-1.094-1.453-1.453-2.298z">
                    </path>
                    <path
                         d="M18.272 13.485c-0.365-0.365-0.723-0.602-1.21-0.845-0.48-0.243-0.966-0.243-1.446-0.243s-0.966 0.122-1.446 0.243c-0.48 0.243-0.845 0.48-1.21 0.845s-0.602 0.723-0.845 1.21c-0.243 0.48-0.365 0.966-0.365 1.568s0.122 1.088 0.365 1.568 0.48 0.845 0.845 1.21c0.365 0.365 0.723 0.602 1.21 0.845s0.966 0.243 1.446 0.243 0.966-0.122 1.446-0.243c0.48-0.243 0.845-0.48 1.21-0.845s0.602-0.723 0.845-1.21c0.243-0.48 0.365-0.966 0.365-1.568s-0.122-1.088-0.365-1.568c-0.243-0.486-0.486-0.845-0.845-1.21z">
                    </path>
                    <path
                         d="M30.938 10.349c-0.845-0.845-1.933-1.21-3.501-1.21h-5.67v13.638h3.501v-4.467h2.054c1.568 0 2.656-0.365 3.501-1.21s1.21-1.933 1.21-3.379c0.115-1.44-0.25-2.528-1.094-3.373zM26.477 15.418h-1.21v-3.379h1.21c1.325 0 1.933 0.602 1.933 1.69s-0.608 1.69-1.933 1.69z">
                    </path>
               </symbol>


               <!-- offbeat -->
               <symbol id="vj_offbeat" viewBox="0 0 32 32">
                    <path
                         d="M27.063 1.25h-22.125c-0 0-0.001 0-0.001 0-1.018 0-1.843 0.825-1.843 1.843 0 0 0 0.001 0 0.001v-0 25.813c0 0 0 0.001 0 0.001 0 1.018 0.825 1.843 1.843 1.843 0 0 0.001 0 0.001 0h22.125c0 0 0.001 0 0.001 0 1.018 0 1.843-0.825 1.843-1.843 0-0 0-0.001 0-0.001v0-25.813c0-0 0-0.001 0-0.001 0-1.018-0.825-1.843-1.843-1.843-0 0-0.001 0-0.001 0h0zM25.219 27.063h-18.438v-22.125h18.438z">
                    </path>
                    <path
                         d="M12.313 12.313h7.375c1.018 0 1.844-0.825 1.844-1.844s-0.825-1.844-1.844-1.844v0h-7.375c-1.018 0-1.844 0.825-1.844 1.844s0.825 1.844 1.844 1.844v0z">
                    </path>
                    <path
                         d="M12.313 19.688h7.375c1.018 0 1.844-0.825 1.844-1.844s-0.825-1.844-1.844-1.844v0h-7.375c-1.018 0-1.844 0.825-1.844 1.844s0.825 1.844 1.844 1.844v0z">
                    </path>
               </symbol>
               <!-- vj_auto -->
               <symbol id="vj_auto" viewBox="0 0 32 32">
                    <path
                         d="M27.953 13.396l-2.195-6.272c-0.598-1.709-2.218-2.858-4.029-2.858h-11.458c-1.811 0-3.43 1.149-4.028 2.857l-2.195 6.272c-1.172 0.771-1.915 2.103-1.915 3.569v7.569c0 1.179 0.955 2.133 2.133 2.133s2.133-0.955 2.133-2.133v-1.345c0 0 5.633 0.278 9.6 0.278s9.6-0.278 9.6-0.278v1.345c0 1.179 0.955 2.133 2.133 2.133s2.133-0.955 2.133-2.133v-7.569c0-1.466-0.743-2.798-1.914-3.568zM7.035 11.321l1.222-3.492c0.3-0.855 1.107-1.428 2.014-1.428h11.458c0.907 0 1.714 0.573 2.014 1.428l1.222 3.492c0.192 0.549-0.266 1.103-0.841 1.010-2.092-0.338-4.781-0.597-8.125-0.597s-6.033 0.259-8.125 0.597c-0.575 0.093-1.033-0.461-0.841-1.010zM6.933 19.2c-0.883 0-1.6-0.717-1.6-1.6s0.717-1.6 1.6-1.6 1.6 0.717 1.6 1.6-0.717 1.6-1.6 1.6zM19.2 18.133h-6.4c-0.589 0-1.067-0.478-1.067-1.067s0.478-1.067 1.067-1.067h6.4c0.589 0 1.067 0.478 1.067 1.067s-0.478 1.067-1.067 1.067zM25.067 19.2c-0.883 0-1.6-0.717-1.6-1.6s0.717-1.6 1.6-1.6 1.6 0.717 1.6 1.6-0.717 1.6-1.6 1.6z">
                    </path>
               </symbol>
               <!-- vj_world_web -->
               <symbol id="vj_world_web" viewBox="0 0 32 32">
                    <path
                         d="M16 0c-8.837 0-16 7.163-16 16s7.163 16 16 16c8.837 0 16-7.163 16-16v0c-0.009-8.833-7.167-15.991-15.999-16h-0.001zM16.046 27.995c-0.007 0-0.013 0.002-0.020 0.002-0.535-0.173-1.608-1.89-2.323-5.079 0.766 0.043 1.533 0.082 2.296 0.082s1.533-0.039 2.3-0.082c-0.708 3.185-1.762 4.9-2.254 5.077zM16 19c-1.031 0-1.985-0.044-2.885-0.115-0.071-0.9-0.115-1.855-0.115-2.885s0.044-1.985 0.115-2.885c0.9-0.071 1.854-0.115 2.885-0.115s1.985 0.044 2.885 0.115c0.071 0.9 0.115 1.854 0.115 2.885s-0.044 1.985-0.115 2.885c-0.9 0.071-1.855 0.115-2.885 0.115zM4.005 16.046c0-0.007-0.002-0.013-0.002-0.020 0.173-0.535 1.89-1.608 5.079-2.323-0.043 0.766-0.082 1.533-0.082 2.296s0.039 1.533 0.082 2.3c-3.185-0.708-4.9-1.762-5.077-2.254zM15.954 4.005c0.007 0 0.013-0.002 0.020-0.002 0.535 0.173 1.608 1.89 2.323 5.079-0.766-0.043-1.533-0.082-2.296-0.082s-1.533 0.039-2.3 0.082c0.708-3.185 1.762-4.9 2.254-5.077zM22.918 13.7c3.185 0.708 4.9 1.762 5.077 2.254 0 0.007 0.002 0.013 0.002 0.020-0.173 0.535-1.89 1.608-5.079 2.323 0.043-0.766 0.082-1.533 0.082-2.296s-0.039-1.533-0.082-2.3zM26.674 10.63c-1.193-0.436-2.616-0.81-4.081-1.056l-0.146-0.020c-0.266-1.612-0.641-3.034-1.131-4.401l0.054 0.174c2.299 1.179 4.125 3.005 5.272 5.237l0.032 0.067zM10.63 5.326c-0.436 1.193-0.81 2.616-1.056 4.081l-0.020 0.146c-1.612 0.266-3.034 0.64-4.401 1.131l0.174-0.054c1.178-2.299 3.004-4.125 5.236-5.272l0.067-0.032zM5.327 21.37c1.193 0.436 2.615 0.81 4.081 1.056l0.146 0.020c0.266 1.611 0.64 3.034 1.131 4.401l-0.054-0.174c-2.299-1.178-4.125-3.004-5.272-5.236l-0.032-0.067zM21.37 26.673c0.436-1.193 0.81-2.615 1.056-4.081l0.020-0.146c1.612-0.266 3.034-0.64 4.401-1.131l-0.174 0.054c-1.179 2.299-3.004 4.125-5.236 5.272l-0.067 0.032z">
                    </path>
               </symbol>
               <!-- vj_cities -->
               <symbol id="vj_cities" viewBox="0 0 32 32">
                    <path
                         d="M16 2.25c-5.693 0.006-10.306 4.62-10.313 10.312v0.001c0 9.312 8.862 16.51 9.238 16.812 0.292 0.234 0.666 0.376 1.074 0.376s0.783-0.142 1.078-0.379l-0.003 0.003c0.376-0.302 9.238-7.499 9.238-16.812-0.006-5.693-4.62-10.306-10.312-10.313h-0.001zM16 25.725c-2.172-2.075-6.875-7.251-6.875-13.163 0-3.797 3.078-6.875 6.875-6.875s6.875 3.078 6.875 6.875v0c0 5.912-4.703 11.088-6.875 13.163z">
                    </path>
                    <path
                         d="M16 9.125c-1.898 0-3.438 1.539-3.438 3.438s1.539 3.438 3.438 3.438c1.898 0 3.438-1.539 3.438-3.438v0c-0.003-1.897-1.54-3.435-3.437-3.438h-0z">
                    </path>
               </symbol>
               <!-- vj_south -->
               <symbol id="vj_south" viewBox="0 0 32 32">
                    <path
                         d="M31.941 10.591c-0.044-0.809-0.691-1.456-1.5-1.5-1.394-0.078-2.803 0.003-4.194 0.244-0.472-1.763-1.038-2.947-1.063-3-0.353-0.731-1.197-1.081-1.962-0.813-0.072 0.025-1.637 0.581-3.503 1.747-1.241-1.741-2.425-2.819-2.566-2.947-0.606-0.541-1.519-0.541-2.125 0-0.141 0.125-1.316 1.197-2.547 2.922-1.847-1.15-3.391-1.697-3.463-1.722-0.766-0.269-1.609 0.081-1.963 0.813-0.025 0.053-0.594 1.244-1.066 3.009-1.409-0.247-2.837-0.331-4.25-0.253-0.813 0.044-1.456 0.691-1.5 1.503-0.206 3.781 0.75 9.003 4.063 12.313 2.6 2.6 6.894 4.091 11.788 4.091h0.003c4.894 0 9.191-1.491 11.787-4.091 3.316-3.316 4.272-8.534 4.059-12.316zM21.678 10.769c-0.103-0.253-0.216-0.506-0.334-0.759 0.556-0.35 1.081-0.637 1.528-0.859 0.097 0.291 0.2 0.625 0.297 0.994-0.519 0.184-1.016 0.394-1.491 0.625zM22.547 13.9c0.909-0.497 1.947-0.894 3.087-1.178 1.016-0.256 2.087-0.412 3.137-0.459-0.063 1.409-0.306 2.853-0.706 4.131-0.556 1.766-1.375 3.2-2.438 4.262v0c-0.772 0.772-1.794 1.428-3.028 1.95-0.844 0.353-1.759 0.634-2.734 0.834 1.425-2.050 2.794-4.834 2.794-7.981-0.003-0.516-0.041-1.034-0.113-1.559zM19.475 15.456c0 3.228-2.106 6.162-3.381 7.644-1.275-1.481-3.381-4.416-3.381-7.644s2.106-6.162 3.381-7.644c1.272 1.481 3.381 4.419 3.381 7.644zM12.319 23.441c-0.975-0.2-1.891-0.481-2.734-0.834-1.238-0.519-2.256-1.175-3.031-1.95v0c-1.059-1.059-1.878-2.494-2.431-4.259-0.4-1.278-0.647-2.725-0.709-4.134 1.094 0.050 2.209 0.216 3.259 0.491 1.078 0.281 2.094 0.675 2.962 1.147-0.075 0.522-0.109 1.044-0.109 1.556 0 3.147 1.369 5.934 2.794 7.984zM9.069 10.162c0.1-0.378 0.206-0.719 0.303-1.016 0.431 0.216 0.941 0.494 1.478 0.831-0.125 0.262-0.241 0.525-0.35 0.787-0.453-0.219-0.934-0.422-1.431-0.603z">
                    </path>
               </symbol>
               <!-- vj_opinion -->
               <symbol id="vj_opinion" viewBox="0 0 32 32">
                    <path
                         d="M26.938 3.5h-21.875c-0.859 0-1.563 0.703-1.563 1.563 0 0 0 0 0 0v15.625c0 0.859 0.703 1.563 1.563 1.563 0 0 0 0 0 0h4.688v4.688c0 0.859 0.703 1.563 1.563 1.563 0.417 0 0.807-0.156 1.094-0.469l5.807-5.781h8.724c0.859 0 1.563-0.703 1.563-1.563 0 0 0 0 0 0v-15.625c0-0.859-0.703-1.563-1.563-1.563 0 0 0 0 0 0zM24.854 18.604h-7.292c-0.417 0-0.807 0.156-1.094 0.469l-3.594 3.568v-2.474c0-0.859-0.703-1.563-1.563-1.563 0 0 0 0 0 0h-4.167v-11.458h17.708v11.458z">
                    </path>
               </symbol>
               <!-- vj_notification -->
               <symbol id="vj_notification" viewBox="0 0 32 32">
                    <path
                         d="M26.705 18.773l-0.58-0.451c-0.322-0.258-0.451-0.645-0.516-1.032v-5.159c0-4.643-3.289-8.577-7.803-9.48-0.258-1.032-1.29-1.677-2.386-1.419-0.709 0.194-1.225 0.709-1.419 1.419-4.385 0.903-7.674 4.837-7.674 9.48v5.224c0 0.387-0.194 0.774-0.516 1.032l-0.58 0.451c-1.29 1.032-2.128 2.709-2.128 4.45v1.096c0 1.419 1.161 2.58 2.58 2.58h5.353c0.709 2.773 3.547 4.385 6.32 3.676 1.806-0.451 3.225-1.87 3.676-3.676h5.288c1.419 0 2.58-1.161 2.58-2.58v-1.032c0-1.806-0.774-3.483-2.193-4.579zM16 27.608c-0.903 0-1.096 0.129-1.548-0.645h3.16c-0.516 0.774-0.709 0.645-1.612 0.645zM25.029 23.094h-18.057v-0.387c0-0.967 0.451-1.29 1.225-1.87l0.58-0.451c0.903-0.709 1.419-1.87 1.419-3.031v-3.934c0-3.934 1.87-7.094 5.804-7.094s5.804 3.16 5.804 7.094v3.934c0 1.161 0.516 2.257 1.419 3.031l0.58 0.451c0.774 0.58 1.225 0.903 1.225 1.87v0.387z">
                    </path>
               </symbol>
               <!-- vj_elections -->
               <symbol id="vj_elections" viewBox="0 0 32 32">
                    <path
                         d="M28.225 12.122c-0.053-0.347-0.222-0.656-0.481-0.884v-0.006l-2.313-1.706c0.413-0.647 0.259-1.516-0.369-1.978l-2.209-1.628 0.047-0.063c0.481-0.653 0.344-1.578-0.313-2.063l-3.397-2.503c-0.316-0.234-0.706-0.331-1.094-0.272-0.391 0.059-0.731 0.266-0.966 0.581l-0.047 0.063-2.209-1.625c-0.653-0.481-1.578-0.344-2.063 0.313l-2.784 3.778-0.653-0.35c-0.366-0.194-0.797-0.228-1.184-0.091-0.391 0.138-0.706 0.434-0.866 0.812l-3.447 8.125c-0.197 0.466-0.144 0.991 0.141 1.409l6.262 9.166-0.991 7.363c-0.109 0.806 0.459 1.55 1.266 1.656 0.819 0.109 1.55-0.472 1.656-1.266l1.066-7.922c0.050-0.363-0.037-0.728-0.244-1.028l-6.128-8.966 2.503-5.897 6.369 3.406-0.547 0.744-2.209-1.628c-0.316-0.234-0.706-0.331-1.094-0.272-0.391 0.059-0.731 0.266-0.966 0.581-0.481 0.653-0.344 1.578 0.313 2.063l3.294 2.428v0.125h0.169l3.313 2.444 0.019 0.019 0.019 0.009 3.375 2.488c0.256 0.188 0.556 0.288 0.875 0.288 0.097 0 0.191-0.009 0.288-0.028l-0.106 0.891-2.3 2.481c-0.269 0.291-0.409 0.684-0.387 1.078l0.356 6.6c0.044 0.781 0.688 1.394 1.469 1.394 0 0 0 0 0 0 0.028 0 0.056 0 0.081-0.003 0.394-0.022 0.753-0.194 1.019-0.488 0.262-0.294 0.397-0.672 0.375-1.063l-0.325-5.978 2.194-2.381c0.209-0.228 0.341-0.512 0.378-0.822l0.697-5.753 1.875-2.544c0.238-0.319 0.331-0.706 0.275-1.097zM15.334 4.037l-1.547 2.1-1.131-0.606 1.656-2.247 1.022 0.753zM24.706 12.653l-2.684 3.641-1.022-0.753 2.684-3.641 1.022 0.753zM19.066 10.634l0.2 0.147 1.837-2.491 1.022 0.753-3.5 4.747-1.022-0.753 1.663-2.256-0.2-0.147zM19.65 5.294l-2.106 2.856-1.131-0.606 2.216-3.003 1.022 0.753z">
                    </path>
               </symbol>
               <!-- vj_business -->
               <symbol id="vj_business" viewBox="0 0 32 32">
                    <path
                         d="M30 6.75h-8c-1.105 0-2 0.895-2 2s0.895 2 2 2v0h3.172l-7.172 7.172-6.586-6.586c-0.362-0.362-0.862-0.586-1.414-0.586s-1.052 0.224-1.414 0.586l-8 8c-0.36 0.361-0.582 0.86-0.582 1.41 0 1.104 0.895 2 2 2 0.55 0 1.049-0.222 1.41-0.582l6.586-6.586 6.586 6.586c0.362 0.362 0.862 0.586 1.414 0.586s1.052-0.224 1.414-0.586l8.586-8.586v3.172c0 1.105 0.895 2 2 2s2-0.895 2-2v0-8c0-0 0-0.001 0-0.001 0-1.104-0.895-1.999-1.999-1.999-0 0-0.001 0-0.001 0h0z">
                    </path>
               </symbol>
               <!-- vj_food -->
               <symbol id="vj_food" viewBox="0 0 32 32">
                    <path
                         d="M14 0c-1.104 0-2 0.894-2 2v10h-2v-10c0-1.105-0.896-2-2-2s-2 0.894-2 2v10h-2v-10c0-1.105-0.896-2-2-2s-2 0.894-2 2v12c0 1.105 0.895 2 2 2h4v14c0 1.105 0.896 2 2 2s2-0.895 2-2v-14h4c1.104 0 2-0.895 2-2v-12c0-1.105-0.896-2-2-2z">
                    </path>
                    <path
                         d="M26 0c-3.314 0-6 2.686-6 6 0 2.609 1.675 4.807 4 5.633v18.367c0 1.105 0.895 2 2 2s2-0.895 2-2v-18.367c2.325-0.826 4-3.023 4-5.633 0-3.314-2.686-6-6-6z">
                    </path>
               </symbol>
               <!-- vj_doctor -->
               <symbol id="vj_doctor" viewBox="0 0 32 32">
                    <path
                         d="M28.667 8.667h-5.333v-5.333c0-1.467-1.2-2.667-2.667-2.667h-9.333c-1.467 0-2.667 1.2-2.667 2.667v5.333h-5.333c-1.467 0-2.667 1.2-2.667 2.667v9.333c0 1.467 1.2 2.667 2.667 2.667h5.333v5.333c0 1.467 1.2 2.667 2.667 2.667h9.333c1.467 0 2.667-1.2 2.667-2.667v-5.333h5.333c1.467 0 2.667-1.2 2.667-2.667v-9.333c0-1.467-1.2-2.667-2.667-2.667zM4.667 19.333v-6.667h8v-8h6.667v8h8v6.667h-8v8h-6.667v-8h-8z">
                    </path>
               </symbol>
               <!-- vj_education -->
               <symbol id="vj_education" viewBox="0 0 32 32">
                    <path
                         d="M29.827 16.532v-2.268c0-0.891-0.729-1.62-1.62-1.62-1.718 0-3.298 0.133-4.813 0.405-0.636-0.561-1.36-1.024-2.135-1.377 1.007-1.215 1.568-2.748 1.568-4.351 0-3.795-3.060-6.885-6.827-6.885s-6.827 3.089-6.827 6.885c0 1.603 0.561 3.136 1.568 4.351-0.775 0.353-1.498 0.816-2.135 1.377-1.516-0.272-3.095-0.405-4.813-0.405-0.891 0-1.62 0.729-1.62 1.62v2.268c-1.059 0.584-1.736 1.707-1.736 2.939v1.736c0 1.232 0.677 2.355 1.736 2.939v2.268c0 0.891 0.729 1.62 1.62 1.62 4.38 0 7.978 1.036 11.31 3.257 0.272 0.179 0.584 0.272 0.897 0.272s0.625-0.093 0.897-0.272c3.332-2.222 6.931-3.257 11.31-3.257 0.891 0 1.62-0.729 1.62-1.62v-2.268c1.059-0.584 1.736-1.707 1.736-2.939v-1.736c0-1.232-0.677-2.355-1.736-2.939zM26.587 16.532c-1.059 0.584-1.736 1.707-1.736 2.939v1.736c0 1.232 0.677 2.355 1.736 2.939v0.694c-3.286 0.179-6.237 0.937-8.967 2.297v-8.504c2.713-1.655 5.519-2.499 8.967-2.696v0.596zM28.091 19.471c0-0.064 0.052-0.116 0.116-0.116s0.116 0.052 0.116 0.116v1.736c0 0.064-0.052 0.116-0.116 0.116s-0.116-0.052-0.116-0.116v-1.736zM14.264 14.149h3.471c0.434 0 0.862 0.052 1.279 0.156-1.030 0.417-2.031 0.92-3.014 1.516-0.983-0.596-1.979-1.093-3.014-1.516 0.417-0.104 0.845-0.156 1.279-0.156zM16 3.677c1.979 0 3.587 1.637 3.587 3.645 0 1.979-1.608 3.587-3.587 3.587s-3.587-1.608-3.587-3.587c0-2.007 1.608-3.645 3.587-3.645zM5.413 24.146c1.059-0.584 1.736-1.707 1.736-2.939v-1.736c0-1.232-0.677-2.355-1.736-2.939v-0.602c3.448 0.197 6.254 1.041 8.967 2.696v8.51c-2.731-1.36-5.681-2.112-8.967-2.297v-0.694zM3.909 19.471v1.736c0 0.064-0.052 0.116-0.116 0.116s-0.116-0.052-0.116-0.116v-1.736c0-0.064 0.052-0.116 0.116-0.116s0.116 0.052 0.116 0.116z">
                    </path>
               </symbol>
               <!-- vj_science -->
               <symbol id="vj_science" viewBox="0 0 32 32">
                    <path
                         d="M18.564 16c0 1.416-1.148 2.564-2.564 2.564s-2.564-1.148-2.564-2.564c0-1.416 1.148-2.564 2.564-2.564s2.564 1.148 2.564 2.564z">
                    </path>
                    <path
                         d="M29.38 19.368c-0.473-1.054-1.259-2.188-2.342-3.368 1.083-1.18 1.869-2.314 2.342-3.368 0.724-1.624 0.724-3.089-0.006-4.348-0.855-1.487-2.439-1.978-3.613-2.131-1.197-0.154-2.621-0.057-4.234 0.285-0.513-1.578-1.14-2.861-1.869-3.835-0.724-0.963-1.943-2.103-3.659-2.103s-2.935 1.14-3.653 2.097c-0.735 0.974-1.362 2.257-1.875 3.835-1.613-0.342-3.037-0.439-4.234-0.279-1.174 0.154-2.758 0.644-3.613 2.131-0.73 1.259-0.73 2.724-0.006 4.354 0.473 1.054 1.259 2.188 2.342 3.368-1.083 1.18-1.869 2.314-2.342 3.368-0.724 1.624-0.724 3.089 0.006 4.348v0c0.724 1.248 1.983 1.977 3.75 2.166 1.151 0.12 2.524 0.006 4.092-0.336 0.513 1.578 1.14 2.872 1.869 3.847 0.724 0.963 1.943 2.108 3.664 2.108 1.715 0 2.941-1.145 3.664-2.108 0.73-0.974 1.356-2.262 1.869-3.841 1.567 0.348 2.941 0.462 4.092 0.336 1.767-0.188 3.032-0.918 3.755-2.166 0.724-1.265 0.724-2.73 0-4.359zM5.686 10.045v0c0.216-0.376 0.963-0.45 1.39-0.467 0.051 0 0.108 0 0.165 0 0.655 0 1.464 0.108 2.388 0.313-0.131 0.735-0.234 1.493-0.319 2.274-0.627 0.462-1.231 0.935-1.795 1.408-1.755-1.858-2.114-3.032-1.829-3.527zM5.686 21.955c-0.279-0.484 0.085-1.653 1.841-3.522 0.564 0.473 1.163 0.94 1.784 1.402 0.085 0.792 0.188 1.561 0.319 2.302-2.576 0.518-3.767 0.125-3.943-0.182zM16 4.033c0.336 0 1.282 0.872 2.126 3.391-0.701 0.256-1.408 0.541-2.126 0.861-0.718-0.319-1.43-0.604-2.126-0.861 0.843-2.519 1.789-3.391 2.126-3.391zM16 27.967c-0.336 0-1.294-0.883-2.137-3.419 0.701-0.256 1.419-0.541 2.137-0.855 0.718 0.313 1.436 0.598 2.137 0.855-0.843 2.536-1.801 3.419-2.137 3.419zM15.972 20.787c-2.627 0-4.758-2.131-4.758-4.758s2.131-4.758 4.758-4.758c2.627 0 4.758 2.131 4.758 4.758s-2.131 4.758-4.758 4.758zM26.314 10.045v0c0.279 0.484-0.085 1.653-1.841 3.522-0.564-0.473-1.163-0.94-1.784-1.402-0.085-0.786-0.188-1.556-0.319-2.297 2.485-0.57 3.681-0.279 3.943 0.177zM26.314 21.955v0c-0.177 0.308-1.368 0.701-3.949 0.177 0.131-0.741 0.239-1.51 0.319-2.302 0.627-0.462 1.231-0.935 1.795-1.408 1.761 1.863 2.12 3.037 1.835 3.533z">
                    </path>
               </symbol>
               <!-- vj_swirlster -->
               <symbol id="vj_swirlster" viewBox="0 0 32 32">
                    <path
                         d="M18.212 31.406h-0.413c-0.413 0-0.413 0-0.963-0.413 0 0-0.413 0-0.413-0.413l-0.55-0.55c0-0.413-0.413-0.413-0.413-0.963 0-0.413 0-0.413-0.413-0.963 0-0.413-0.413-0.963-0.413-0.963 0-0.413 0-0.963 0-0.963v-0.413c-0.413-0.413 0-0.963 0-1.376 0.413 0 0.413-0.413 0.413-0.963 0 0 0 0 0 0.413s0.413 0.963 0.413 0.963 0 0 0 0.413c0 0.413 0.413 0.963 0.413 1.376v0.413c0.413 0.413 0.413 0.963 0.413 1.376s0 0.963 0.413 0.963c0 0.413 0 0.963 0 0.963 0 0.413 0 0.413-0.413 0.413l1.926 0.688zM22.751 8.572c0-0.413 0-0.413-0.413-0.413s-0.413 0.413-0.963 0.413c-0.413 0.413-0.413 0.413-0.963 0.963-0.413 0.413-0.963 0.413-1.376 0.963-0.413 0.413-0.963 0.413-1.376 0.963 0 0 0 0-0.413 0.413-0.963 0.413-1.376 1.376-1.926 1.926 0 0 0 0-0.413 0h-0.55c-0.413-0.413-0.963-1.376-0.963-1.926 0 0 0-0.413-0.413-0.413 0-0.413-0.413-0.963-0.413-1.376s0-0.413-0.413-0.963c0-0.413-0.413-1.376-0.413-1.926v-0.825c0-0.413 0-0.413 0-0.413v-0.413c0-0.413 0-0.963 0-1.376 0 0 0-0.413 0.413-0.413h0.413l0.413 0.413v0.825c0.413 0.413 0.413 0.963 0.413 1.926 0 0.413 0 0.963 0.413 1.376 0 0 0 0 0-0.413s0-0.963 0.413-0.963c0.413-0.413 0.413-0.413 0.413-0.963 0-0.413 0-0.963 0-1.376s0-0.963 0-1.376c0 0 0 0 0-0.413s0-0.963-0.413-1.376-0.963-0.963-1.926-0.963c-0.413 0-0.413 0-0.963 0.413-0.413 0-0.963 0.413-0.963 0.413-0.413 0-0.963 0.413-1.376 0.413-0.413 0.413-0.963 0.413-0.963 0.963 0 0 0 0 0 0.413 0 0 0 0 0 0.413s0 0.413 0 0.963c0 0.413 0 0.413 0 0.963v0.413c0 0.413 0 1.376 0.413 1.926v0.825c0.413 0.413 0.413 0.963 0.413 1.376s0 0.413 0 0.963c0 0.413 0.413 0.963 0.413 1.376s0.413 0.963 0.413 1.376c0.413 0.413 0.413 1.376 0.963 1.926 0 0.413 0.413 0.963 0.413 0.963 0 0.413 0 0.413 0.413 0.963 0 0.413 0.413 0.963 0.963 0.963 0 0.413 0 0.963-0.413 1.376 0 0.413-0.413 0.963-0.413 1.376 0 0.963-0.413 2.338-0.413 3.301s0 2.338 0.413 3.301c0 0.413 0 0.413 0.413 0.963v0.413c0.413 0.413 0.413 0.413 0.413 0.963 0 0.413 0.413 0.413 0.413 0.963 0 0 0 0 0.413 0 0 0 0.413 0 0.413 0.413 0 0 0 0.413 0.413 0.413s0.413 0 0.963 0 1.376 0 1.926 0c0.413 0 0.963 0 0.963 0 0.413 0 0.963-0.413 1.376-0.413 0.413-0.413 0.963-0.413 0.963-0.413 0.413 0 0.413-0.413 0.413-0.963 0-0.413 0-0.963 0-1.376 0-0.963 0-1.376 0-1.926s0-0.413 0-0.963c-0.413-0.413-0.963-1.376-0.963-1.926-0.413-0.413-0.963-1.376-0.963-1.926-0.413-0.413-0.413-0.963-0.963-1.376-0.413-0.413-0.413-0.963-0.963-1.926-0.413-0.413-0.963-1.376-0.963-1.926v-0.413c0-0.963 0-1.376 0.963-1.926l0.413-0.413c0-0.413 0.413-0.413 0.413-0.963l0.413-0.413c0.413-0.963 1.376-1.926 2.338-2.338 0.413-0.413 0.963-0.963 0.963-1.376s0.413-0.413 0.413-0.963c0-0.413 0-0.413 0-0.963v1.513z">
                    </path>
               </symbol>
               <!-- vj_photos -->
               <symbol id="vj_photos" viewBox="0 0 32 32">
                    <path
                         d="M29.5 6.357h-6.522l-1.396-2.791c-0.324-0.637-0.974-1.066-1.725-1.066h-7.715c-0.751 0-1.401 0.429-1.72 1.055l-0.005 0.011-1.396 2.791h-6.522c-0 0-0.001 0-0.001 0-1.065 0-1.927 0.863-1.927 1.928 0 0 0 0.001 0 0.001v-0 19.286c0 0 0 0.001 0 0.001 0 1.064 0.863 1.927 1.927 1.927 0 0 0.001 0 0.001 0h27c0 0 0.001 0 0.001 0 1.064 0 1.927-0.863 1.927-1.927 0-0 0-0.001 0-0.001v0-19.286c0-0 0-0.001 0-0.001 0-1.064-0.863-1.928-1.927-1.928-0 0-0.001 0-0.001 0h0zM27.571 25.643h-23.143v-15.429h5.786c0.751-0 1.401-0.429 1.72-1.055l0.005-0.011 1.396-2.791h5.33l1.396 2.791c0.324 0.637 0.974 1.066 1.725 1.066h5.786z">
                    </path>
                    <path
                         d="M16 13.107c-2.13 0-3.857 1.727-3.857 3.857s1.727 3.857 3.857 3.857c2.13 0 3.857-1.727 3.857-3.857v0c-0.003-2.129-1.728-3.854-3.857-3.857h-0z">
                    </path>
               </symbol>
               <!-- vj_sports -->
               <symbol id="vj_sports" viewBox="0 0 32 32">
                    <path
                         d="M30.75 4.281h-5.531v-3.031c0-0.947-0.772-1.719-1.719-1.719h-15c-0.947 0-1.719 0.772-1.719 1.719v3.031h-5.531c-0.947 0-1.719 0.772-1.719 1.719v3.75c0 4.347 3.497 7.891 7.825 7.969 0.409 0.919 1.025 1.744 1.797 2.4 0.762 0.65 1.666 1.122 2.628 1.378v2.784h-2.031c-0.781 0-1.463 0.528-1.662 1.281l-1.25 4.75c-0.134 0.512-0.022 1.069 0.3 1.488s0.831 0.669 1.362 0.669h15c0.528 0 1.038-0.25 1.363-0.669 0.322-0.419 0.434-0.975 0.3-1.488l-1.25-4.75c-0.2-0.753-0.881-1.281-1.663-1.281h-2.031v-2.784c0.962-0.256 1.866-0.728 2.628-1.378 0.772-0.656 1.387-1.481 1.797-2.4 4.328-0.078 7.825-3.622 7.825-7.969v-3.75c0-0.947-0.772-1.719-1.719-1.719zM29.031 7.719v2.031c0 1.169-0.447 2.278-1.256 3.125-0.691 0.725-1.584 1.194-2.556 1.347v-6.503h3.813zM16.781 21.719v2.563h-1.563v-2.563h1.563zM18.5 18.281h-5c-1.809 0-3.281-1.472-3.281-3.281v-12.031h11.563v12.031c0 1.809-1.472 3.281-3.281 3.281zM21.272 29.031h-10.544l0.347-1.313h9.85l0.347 1.313zM6.781 7.719v6.506c-0.972-0.156-1.866-0.625-2.556-1.347-0.809-0.85-1.256-1.959-1.256-3.128v-2.031h3.813z">
                    </path>
               </symbol>
               <!-- vj_people -->
               <symbol id="vj_people" viewBox="0 0 32 32">
                    <path
                         d="M26.569 19.248c0.63-0.912 1.006-2.041 1.006-3.258 0-3.19-2.586-5.776-5.776-5.776-2.057 0-3.863 1.075-4.886 2.695l-0.014 0.024c-0.556-0.526-1.18-0.989-1.854-1.374l-0.048-0.025c0.628-0.912 1.003-2.040 1.003-3.255 0-3.195-2.59-5.786-5.786-5.786s-5.786 2.59-5.786 5.786c0 1.216 0.375 2.344 1.015 3.275l-0.013-0.020c-2.915 1.68-4.848 4.774-4.86 8.321v0.002c0 0 0 0.001 0 0.001 0 1.064 0.863 1.927 1.928 1.927 0 0 0.001 0 0.001 0h11.62c-1.227 1.584-1.969 3.598-1.977 5.784v0.002c0 0 0 0.001 0 0.001 0 1.064 0.863 1.927 1.928 1.927 0 0 0.001 0 0.001 0h15.429c0 0 0.001 0 0.001 0 1.064 0 1.927-0.863 1.927-1.927 0-0 0-0.001 0-0.001v0c-0.012-3.549-1.945-6.643-4.813-8.298l-0.046-0.025zM21.786 14.071c1.065 0 1.929 0.863 1.929 1.929s-0.863 1.929-1.929 1.929c-1.065 0-1.929-0.863-1.929-1.929v0c0.002-1.064 0.864-1.927 1.928-1.929h0zM8.286 8.286c0-1.065 0.863-1.929 1.929-1.929s1.929 0.863 1.929 1.929c0 1.065-0.863 1.929-1.929 1.929v0c-1.064-0.002-1.927-0.864-1.929-1.928v-0zM10.214 14.071c2.503 0.002 4.635 1.592 5.442 3.817l0.013 0.040h-10.909c0.82-2.265 2.951-3.855 5.454-3.857h0zM16.332 25.643c0.818-2.266 2.95-3.857 5.454-3.857s4.636 1.591 5.442 3.817l0.013 0.040z">
                    </path>
               </symbol>
               <!-- vj_weather -->
               <symbol id="vj_weather" viewBox="0 0 32 32">
                    <path
                         d="M20.5 17.25c-0.875 0-1.625 0.75-1.625 1.625v8.625c0 0.875 0.75 1.625 1.625 1.625s1.625-0.75 1.625-1.625v-8.625c0-0.875-0.75-1.625-1.625-1.625z">
                    </path>
                    <path
                         d="M11.375 17.25c-0.875 0-1.625 0.75-1.625 1.625v8.625c0 0.875 0.75 1.625 1.625 1.625s1.625-0.75 1.625-1.625v-8.625c0-0.875-0.625-1.625-1.625-1.625z">
                    </path>
                    <path
                         d="M16 19.75c-0.875 0-1.625 0.75-1.625 1.625v8.625c0 0.875 0.75 1.625 1.625 1.625s1.625-0.75 1.625-1.625v-8.625c0-0.875-0.75-1.625-1.625-1.625z">
                    </path>
                    <path
                         d="M28.5 9.375c-1.5-1.375-3.375-2.125-5.375-2-1.375-3.5-4.75-5.75-8.5-5.75-5 0-9 4-9.125 9-2.625 0.875-4.375 3.25-4.375 6 0 3.5 2.75 6.25 6.25 6.25 1 0 1.875-0.875 1.875-1.875s-0.875-1.875-1.875-1.875c-1.375 0-2.5-1.125-2.5-2.5s1.125-2.5 2.375-2.5h2.625l-0.5-2.375c-0.125-0.375-0.125-0.625-0.125-1 0-3 2.375-5.375 5.375-5.375 2.625 0 4.875 1.875 5.25 4.375l0.375 2.125 2-0.625c0.375-0.125 0.75-0.125 1-0.125 2.125 0 3.875 1.75 3.875 3.875 0 1.75-1.125 3.25-2.875 3.75-1 0.25-1.625 1.375-1.375 2.375s1.375 1.625 2.375 1.375c3.375-0.875 5.625-4 5.625-7.375 0.125-2.25-0.75-4.375-2.375-5.75z">
                    </path>
               </symbol>
               <!-- vj_tv-schedule -->
               <symbol id="vj_tv-schedule" viewBox="0 0 32 32">
                    <path
                         d="M27.661 4.819h-2.242v-1.531c0-1.126-0.913-2.039-2.039-2.039h-0.082c-1.126 0-2.039 0.913-2.039 2.039v1.531h-10.519v-1.531c0-1.126-0.913-2.039-2.039-2.039h-0.082c-1.126 0-2.039 0.913-2.039 2.039v1.531h-2.242c-1.126 0-2.039 0.913-2.039 2.039v21.854c0 1.126 0.913 2.039 2.039 2.039h23.321c1.126 0 2.039-0.913 2.039-2.039v-21.854c0-1.126-0.913-2.039-2.039-2.039zM26.274 27.529h-20.549v-16.553h20.549v16.553z">
                    </path>
                    <path
                         d="M8.518 18.467h3.547c0.18 0 0.326-0.146 0.326-0.326v-3.547c0-0.18-0.146-0.326-0.326-0.326h-3.547c-0.18 0-0.326 0.146-0.326 0.326v3.547c0 0.18 0.146 0.326 0.326 0.326z">
                    </path>
                    <path
                         d="M14.227 18.467h3.547c0.18 0 0.326-0.146 0.326-0.326v-3.547c0-0.18-0.146-0.326-0.326-0.326h-3.547c-0.18 0-0.326 0.146-0.326 0.326v3.547c0 0.18 0.146 0.326 0.326 0.326z">
                    </path>
                    <path
                         d="M19.935 18.467h3.547c0.18 0 0.326-0.146 0.326-0.326v-3.547c0-0.18-0.146-0.326-0.326-0.326h-3.547c-0.18 0-0.326 0.146-0.326 0.326v3.547c0 0.18 0.146 0.326 0.326 0.326z">
                    </path>
                    <path
                         d="M8.518 24.175h3.547c0.18 0 0.326-0.146 0.326-0.326v-3.547c0-0.18-0.146-0.326-0.326-0.326h-3.547c-0.18 0-0.326 0.146-0.326 0.326v3.547c0 0.18 0.146 0.326 0.326 0.326z">
                    </path>
                    <path
                         d="M14.227 24.175h3.547c0.18 0 0.326-0.146 0.326-0.326v-3.547c0-0.18-0.146-0.326-0.326-0.326h-3.547c-0.18 0-0.326 0.146-0.326 0.326v3.547c0 0.18 0.146 0.326 0.326 0.326z">
                    </path>
                    <path
                         d="M19.935 24.175h3.547c0.18 0 0.326-0.146 0.326-0.326v-3.547c0-0.18-0.146-0.326-0.326-0.326h-3.547c-0.18 0-0.326 0.146-0.326 0.326v3.547c0 0.18 0.146 0.326 0.326 0.326z">
                    </path>
               </symbol>
               <!-- vj_trains -->
               <symbol id="vj_trains" viewBox="0 0 21 32">
                    <path
                         d="M10.105 1.347c0 0.558-0.452 1.011-1.011 1.011s-1.011-0.452-1.011-1.011c0-0.558 0.452-1.011 1.011-1.011s1.011 0.452 1.011 1.011z">
                    </path>
                    <path
                         d="M12.8 1.347c0 0.558-0.452 1.011-1.011 1.011s-1.011-0.452-1.011-1.011c0-0.558 0.452-1.011 1.011-1.011s1.011 0.452 1.011 1.011z">
                    </path>
                    <path
                         d="M15.158 2.695h-9.432c-2.419 0-4.379 1.96-4.379 4.379v13.474c0 2.419 1.96 4.379 4.379 4.379h9.432c2.419 0 4.379-1.96 4.379-4.379v-13.474c0-2.419-1.96-4.379-4.379-4.379zM7.747 4.042c0-0.371 0.303-0.674 0.674-0.674h4.042c0.371 0 0.674 0.303 0.674 0.674v1.347c0 0.371-0.303 0.674-0.674 0.674h-4.042c-0.371 0-0.674-0.303-0.674-0.674v-1.347zM5.726 22.905c-0.93 0-1.684-0.755-1.684-1.684s0.755-1.684 1.684-1.684 1.684 0.755 1.684 1.684-0.755 1.684-1.684 1.684zM15.158 22.905c-0.93 0-1.684-0.755-1.684-1.684s0.755-1.684 1.684-1.684 1.684 0.755 1.684 1.684-0.755 1.684-1.684 1.684zM17.179 11.453c0 1.118-0.903 2.021-2.021 2.021h-9.432c-1.118 0-2.021-0.903-2.021-2.021v-2.695c0-1.118 0.903-2.021 2.021-2.021h9.432c1.118 0 2.021 0.903 2.021 2.021v2.695z">
                    </path>
                    <path d="M0 32l4.716-7.747h11.453l4.716 7.747h-3.032l-3.032-5.053h-8.758l-3.032 5.053z"></path>
               </symbol>
               <!-- vj_art -->
               <symbol id="vj_art" viewBox="0 0 32 32">
                    <path
                         d="M30.179 20.439v-16.275c0.74-0.247 1.233-0.863 1.233-1.726 0-1.11-0.74-1.849-1.849-1.849h-27.125c-1.11 0-1.849 0.74-1.849 1.849 0 0.863 0.493 1.48 1.233 1.726v16.151c-0.74 0.247-1.233 0.863-1.233 1.726 0 1.11 0.74 1.849 1.849 1.849h9l-2.096 4.808c-0.37 0.986 0 2.096 0.986 2.466 0.247 0.123 0.493 0.123 0.74 0.123 0.74 0 1.356-0.37 1.726-1.11l2.712-6.288h0.986l2.712 6.288c0.37 0.863 1.48 1.356 2.343 0.986s1.356-1.48 0.986-2.466l-2.096-4.808h9.124c1.11 0 1.849-0.74 1.849-1.849 0-0.74-0.493-1.356-1.233-1.603zM11.068 16.863l2.466 2.466 6.165-6.165 6.781 6.781v0.37h-18.864l3.452-3.452zM5.52 18.836v-14.549h20.96v12.083l-6.781-6.781-6.165 6.165-2.466-2.466-5.548 5.548z">
                    </path>
                    <path
                         d="M13.534 11.068c1.356 0 2.466-1.11 2.466-2.466s-1.11-2.466-2.466-2.466-2.466 1.11-2.466 2.466 1.11 2.466 2.466 2.466zM13.534 7.369c0.74 0 1.233 0.493 1.233 1.233s-0.493 1.233-1.233 1.233-1.233-0.493-1.233-1.233 0.493-1.233 1.233-1.233z">
                    </path>
               </symbol>
               <!-- vj_close -->
               <symbol id="vj_close" viewBox="0 0 32 32">
                    <path
                         d="M19.625 16l7.938-7.944c1-1 1-2.625 0-3.625-0.488-0.487-1.131-0.75-1.813-0.75s-1.325 0.269-1.813 0.75l-7.938 7.944-7.944-7.938c-1-1-2.625-1-3.625 0s-1 2.625 0 3.625l7.944 7.938-7.938 7.944c-0.487 0.488-0.75 1.131-0.75 1.813s0.269 1.325 0.75 1.813c0.5 0.5 1.156 0.75 1.813 0.75s1.313-0.25 1.813-0.75l7.938-7.944 7.944 7.938c1 1 2.625 1 3.625 0 0.994-1 0.994-2.625 0-3.625l-7.944-7.938z">
                    </path>
               </symbol>
               <!-- vj_search -->
               <symbol id="vj_search" viewBox="0 0 32 32">
                    <title>search</title>
                    <path
                         d="M28.933 27.067l-4.933-4.933c1.6-2 2.667-4.667 2.667-7.467 0-6.667-5.333-12-12-12s-12 5.333-12 12c0 6.667 5.333 12 12 12 2.8 0 5.467-0.933 7.467-2.667l4.933 4.933c0.267 0.267 0.667 0.4 0.933 0.4s0.667-0.133 0.933-0.4c0.533-0.533 0.533-1.333 0-1.867zM5.333 14.667c0-5.2 4.133-9.333 9.333-9.333s9.333 4.133 9.333 9.333c0 2.533-1.067 4.933-2.667 6.533 0 0 0 0 0 0s0 0 0 0c-1.733 1.733-4 2.667-6.533 2.667-5.333 0.133-9.467-4-9.467-9.2z">
                    </path>
               </symbol>
               <symbol xmlns="https://www.w3.org/2000/svg" viewBox="0 0 20 43.97" id="olympic">
                    <path
                         d="M2.19 21h15.62A2.19 2.19 0 0120 23.24a2.19 2.19 0 01-2.19 2.19H2.19A2.19 2.19 0 010 23.26 2.19 2.19 0 012.19 21zm2 5.74h12.3L12 43.43a.74.74 0 01-.71.54H9.43a.74.74 0 01-.71-.54zm4.64-7.13c3.09 0 5.31-2 6.46-4.84C17.29 9.83 13.66 0 9.4 0a7.43 7.43 0 01-.9 9.75C7.9 8.63 8.17 7 8.12 5.59a9 9 0 00-4.91 8.46 5.61 5.61 0 005.61 5.6z">
                    </path>
               </symbol>
               <symbol id="vj_olympic" viewBox="0 0 20 43.97">
                    <title>olympic</title>
                    <path
                         d="M2.19 21h15.62A2.19 2.19 0 0120 23.24a2.19 2.19 0 01-2.19 2.19H2.19A2.19 2.19 0 010 23.26 2.19 2.19 0 012.19 21zm2 5.74h12.3L12 43.43a.74.74 0 01-.71.54H9.43a.74.74 0 01-.71-.54zm4.64-7.13c3.09 0 5.31-2 6.46-4.84C17.29 9.83 13.66 0 9.4 0a7.43 7.43 0 01-.9 9.75C7.9 8.63 8.17 7 8.12 5.59a9 9 0 00-4.91 8.46 5.61 5.61 0 005.61 5.6z">
                    </path>
               </symbol>
               <symbol xmlns="https://www.w3.org/2000/svg" viewBox="0 0 208 208" id="vj_crypto">
                    <title>crypto_icon</title>
                    <path
                         d="M104 208C46.562 208 0 161.438 0 104S46.562 0 104 0s104 46.562 104 104-46.562 104-104 104zm.5-19c46.668 0 84.5-37.832 84.5-84.5S151.168 20 104.5 20 20 57.832 20 104.5 57.832 189 104.5 189zm18.185-121.248c9.715 4.84 17.161 13.426 20.466 23.77l-14.749-.536a27.042 27.042 0 00-22.85-14.156C90.7 76.29 78.26 87.77 77.769 102.47c-.492 14.702 11.149 27.057 26.002 27.597 9.954.362 18.824-4.675 23.74-12.462l14.75.536c-3.989 10.079-11.991 18.103-22.007 22.226l-.567 16.93-13.446-.49.45-13.445a41.317 41.317 0 01-6.723-.245l-.45 13.446-13.447-.489.567-16.93c-13.676-6.813-22.855-21.048-22.315-37.162.54-16.114 10.649-29.648 24.747-35.452l.567-16.93 13.446.49-.45 13.445a41.317 41.317 0 016.723.245l.45-13.446 13.447.489-.567 16.93z">
                    </path>
               </symbol>
               <!-- Facebook -->
               <symbol id="vj_facebook" viewBox="0 0 32 32">
                    <path
                         d="M12.185 7.178v3.965h-2.905v4.849h2.905v14.408h5.967v-14.408h4.004c0 0 0.375-2.325 0.557-4.867h-4.539v-3.315c0-0.495 0.651-1.162 1.294-1.162h3.251v-5.048h-4.42c-6.262-0-6.115 4.853-6.115 5.578z">
                    </path>
               </symbol>

               <!-- Twitter -->
               <symbol id="vj_twitter" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 21.57 19.5">
                         <path d="m16.99,0h3.31l-7.23,8.26,8.5,11.24h-6.66l-5.21-6.82-5.97,6.82H.43l7.73-8.84L0,0h6.83l4.71,6.23L16.99,0Zm-1.16,17.52h1.83L5.83,1.88h-1.97l11.97,15.64Z"></path>
                    </symbol>

               <!-- Instagram -->
               <symbol id="insta" xmlns="https://www.w3.org/2000/svg" viewBox="0 0 510.97 511.1">
                    <path
                         d="M510.5,150.24C509.36,61.49,450.48,2.8,361.86,1.6c-21.67-2.34-189.06-2-210.73-.1C87.13,3.56,37.49,30.77,14.37,88.15-4.6,151.82,3.19,160.48.89,255.55c3.85,103.8-12.64,149.23,42.93,212.63C75.06,497.71,103.54,506.46,151,509.5c21.55,2.19,189,1.93,210.62,0,88.71-1.23,147.36-60,148.64-148.64C512.44,339.32,512.28,171.8,510.5,150.24Zm-46,208.63C455.66,481.7,372,462.62,256.55,465.08,141.11,462.63,57.32,481.76,48.71,359c-2.15-21.21-2-185.25,0-206.44,3-50.4,16-77.13,57.29-95.83,43.63-17.85,204.37-8.6,253.86-8.79C410.24,51,437,63.84,455.7,105.11,473.58,148.81,464.28,309.22,464.48,358.87Zm-208-234.59c-172.55,3-172.52,259.58,0,262.54C429,383.84,429,127.23,256.45,124.28Zm0,216.42c-111.93-1.92-111.91-168.39,0-170.3C368.38,172.32,368.36,338.79,256.45,340.7ZM423.56,119.09c-.69,40.28-60.61,40.28-61.3,0C362.44,79,423.38,79,423.56,119.09Z"
                         transform="translate(-0.89 0.05)"></path>
               </symbol>

               <!-- Linkedin -->
               <symbol id="linkedin" xmlns="https://www.w3.org/2000/svg" viewBox="0 0 512 512">
                    <path
                         d="M511.87,512v0H512V324.2c0-91.86-19.78-162.62-127.17-162.62-51.62,0-86.27,28.33-100.41,55.19h-1.5V170.15H181.1V512h106V342.72c0-44.57,8.44-87.66,63.63-87.66,54.38,0,55.19,50.86,55.19,90.52V512ZM8.45,170.18H114.6V512H8.45ZM61.48,0A61.5,61.5,0,0,0,0,61.48c0,33.94,27.54,62.06,61.48,62.06S123,95.42,123,61.48A61.54,61.54,0,0,0,61.48,0Z">
                    </path>
               </symbol>

               <!-- Youtube -->
               <symbol id="youtube" xmlns="https://www.w3.org/2000/svg" viewBox="0 0 639.37 447.66">
                    <path
                         d="M647.18,181.19a80.11,80.11,0,0,0-56.35-56.36c-50-13.69-250.17-13.69-250.17-13.69s-200.13,0-250.16,13.17c-26.86,7.37-49,29.49-56.35,56.88C21,231.22,21,335,21,335s0,104.28,13.17,153.79A80.08,80.08,0,0,0,90.5,545.11c50.56,13.7,250.17,13.7,250.17,13.7s200.13,0,250.16-13.17a80.14,80.14,0,0,0,56.36-56.36c13.16-50,13.16-153.78,13.16-153.78S660.88,231.22,647.18,181.19ZM276.94,430.83V239.12L443.36,335Z"
                         transform="translate(-20.98 -111.14)"></path>
               </symbol>

               <!-- Koo -->
               <symbol id="koos" xmlns="https://www.w3.org/2000/svg" viewBox="0 0 206.07 300.48">
                    <path
                         d="M205.85,173.4a65.08,65.08,0,0,0-8.41-26,41.85,41.85,0,0,0-4.23-6,1.56,1.56,0,0,0-.79-.49,1.52,1.52,0,0,0-.92.07,1.46,1.46,0,0,0-.7.6,1.49,1.49,0,0,0-.22.9,244.29,244.29,0,0,1-.05,38.73A148.73,148.73,0,0,1,187.86,199a1.44,1.44,0,0,0,0,.77,1.41,1.41,0,0,0,.42.65,1.5,1.5,0,0,0,.69.34,1.44,1.44,0,0,0,.77-.06,25.93,25.93,0,0,0,9-5.16C204.49,190.5,206.85,183,205.85,173.4ZM126.24,28.1a3,3,0,0,0,1.2,0,3,3,0,0,0,1.9-1.38,2.84,2.84,0,0,0,.4-1.13c2.71-17.86-14.87-29.12-18.9-24.51-3.36,3.83,3.7,6.85,4.57,11.3-5.52-3-12.34-4.8-13.48-.61-1,3.88,4.12,5.94,8.83,8.16-3.71.2-8.13.4-10.29,3.77a3,3,0,0,0-.46,1.65,3,3,0,0,0,.51,1.63,3,3,0,0,0,1.33,1.09,2.92,2.92,0,0,0,1.7.18l1.52-.22A72.56,72.56,0,0,1,126.24,28.1ZM184,133.29c-.06-.61-.12-1.22-.17-1.82-.42-4.27-.88-8.35-1.34-12.16-4.35-36.31-15.41-61.55-32.88-75-15-11.59-32.06-12.09-43.74-10.48-20.61,2.85-55.79,17.43-60,83q-.45,7.08-.65,13.51a.77.77,0,0,0,.48.74c2.67,1.16,5.19,3.62,7.35,7.22,6.14,10.2,8.84,28.28,1.73,41.69-6.78,12.78-18.6,17.53-25,19.23h-.13a39.68,39.68,0,0,1-11.42,1.38H13.88c-7.64,0-12.38.64-13.73,5.5-.64,2.3.69,8.72,7,17,5.09,6.71,14.69,16.34,31.48,24.18A124.89,124.89,0,0,0,70.28,257l1.15,3.1c.37,1,.75,2.07,1.13,3.15,2.47,6.86,5.11,14.15,5.93,16.33.32.83,0,1.87-1.54,1.87H67.79s-2.74,6.08,4.72,5.86c20.7-.62,18.45,15.95,25,12.82,6.27-3-5.67-12.85-5.49-12.82,23.85,3,16.23-5.88,16.23-5.88s-12.08.09-16.63,0a6.46,6.46,0,0,1-5.91-4.2l-4.79-13-1.13-3.07-1.13-3A177.45,177.45,0,0,0,99,259.3a133.08,133.08,0,0,0,21.38-1.64c.28.76.63,1.73,1,2.8.32.87.66,1.81,1,2.77,1.37,3.78,2.79,7.72,2.94,8.18.43,1.32.12,1.83-2.23,1.83h-8.86s-2.56,5.71,7.24,5.71c20,0,15.81,16.78,23.5,12.5C149.89,288.7,140.76,281,140,280c-.41-.52-.07-1.26,1-1.1,20.41,3.12,15.4-5.7,15.4-5.7s-14.08.08-20.09.08a2.91,2.91,0,0,1-2.71-1.84c-.86-2.16-2.33-6.26-3.62-9.87l-1-2.73c-.39-1.08-.74-2-1-2.77a86.5,86.5,0,0,0,11-3.44,65.84,65.84,0,0,0,25.46-17.49c6.94-7.81,12.1-17.41,15.58-29,.18-.61.36-1.23.53-1.85l.51-1.86a135.49,135.49,0,0,0,3.68-21.82c1.4-15.31.7-31.3-.58-45.52-.11-.58-.17-1.21-.23-1.86Zm-79-30.89a4.41,4.41,0,0,1-5.32-5A4.41,4.41,0,0,1,101,94.9a4.45,4.45,0,0,1,7.51,4,4.36,4.36,0,0,1-1.22,2.28,4.48,4.48,0,0,1-2.28,1.23Zm36.19,14.7-11.49,7.45a2.31,2.31,0,0,1-1.42.42h0a2.3,2.3,0,0,1-1.41-.42L115.4,117.1a1.84,1.84,0,0,1-.76-.8,1.94,1.94,0,0,1,.25-2.1,2,2,0,0,1,.92-.6l11.31-4.69a3.43,3.43,0,0,1,1.19-.21h0a3.48,3.48,0,0,1,1.2.21l11.3,4.69a1.86,1.86,0,0,1,.93.6,2,2,0,0,1,.45,1,1.92,1.92,0,0,1-.19,1.08,1.83,1.83,0,0,1-.75.81Zm11-14.71a4.51,4.51,0,0,1-2.78-.34,4.47,4.47,0,1,1,2.79.34ZM19.34,194.81h.9a36.69,36.69,0,0,0,8-1.22l.65-.21a37,37,0,0,0,9-3.87,32,32,0,0,0,4.56-3.29,30.89,30.89,0,0,0,7.15-9c5.88-11.1,3.81-27-1.58-35.94a16.12,16.12,0,0,0-3-3.78c-1-.83-1.9-1.48-2.71-1.36a.72.72,0,0,0-.2.09,13.53,13.53,0,0,0-3,2.6,84.81,84.81,0,0,0-8.82,11.9,189.73,189.73,0,0,0-14.6,27.62c-2.57,6.16-3.55,10-3.88,12.22a3.42,3.42,0,0,0,.6,2.5,3.5,3.5,0,0,0,2.16,1.39,24.24,24.24,0,0,0,4.81.35Z"
                         transform="translate(-0.01 -0.05)"></path>
               </symbol>

               <symbol id="vj_earth" viewBox="0 0 32 32">
                    <path
                         d="M27.314 4.686c3.022 3.022 4.686 7.040 4.686 11.314s-1.664 8.292-4.686 11.314c-3.022 3.022-7.040 4.686-11.314 4.686s-8.292-1.664-11.314-4.686c-3.022-3.022-4.686-7.040-4.686-11.314s1.664-8.292 4.686-11.314 7.040-4.686 11.314-4.686c4.274 0 8.292 1.664 11.314 4.686zM25.899 25.9c1.971-1.971 3.281-4.425 3.821-7.096-0.421 0.62-0.824 0.85-1.073-0.538-0.257-2.262-2.335-0.817-3.641-1.621-1.375 0.927-4.466-1.802-3.941 1.276 0.81 1.388 4.375-1.858 2.598 1.079-1.134 2.051-4.145 6.592-3.753 8.946 0.049 3.429-3.504 0.715-4.729-0.422-0.824-2.279-0.281-6.262-2.434-7.378-2.338-0.101-4.344-0.314-5.25-2.927-0.545-1.87 0.58-4.653 2.584-5.083 2.933-1.843 3.98 2.158 6.731 2.232 0.854-0.894 3.182-1.178 3.375-2.18-1.805-0.318 2.29-1.517-0.173-2.199-1.359 0.16-2.234 1.409-1.512 2.467-2.632 0.614-2.717-3.81-5.247-2.414-0.064 2.206-4.132 0.715-1.407 0.268 0.936-0.409-1.527-1.594-0.196-1.379 0.654-0.036 2.854-0.807 2.259-1.325 1.225-0.761 2.255 1.822 3.454-0.059 0.866-1.446-0.363-1.713-1.448-0.98-0.612-0.685 1.080-2.165 2.573-2.804 0.497-0.213 0.972-0.329 1.336-0.296 0.752 0.869 2.142 1.019 2.215-0.104-1.862-0.892-3.915-1.363-6.040-1.363-3.051 0-5.952 0.969-8.353 2.762 0.645 0.296 1.012 0.664 0.39 1.134-0.483 1.439-2.443 3.371-4.163 3.098-0.893 1.54-1.482 3.238-1.733 5.016 1.441 0.477 1.773 1.42 1.464 1.736-0.734 0.64-1.186 1.548-1.418 2.541 0.469 2.87 1.818 5.515 3.915 7.612 2.644 2.644 6.16 4.1 9.899 4.1s7.255-1.456 9.899-4.1z">
                    </path>
               </symbol>

               <symbol xmlns="https://www.w3.org/2000/svg" viewBox="0 0 19 23" id="vj_shopping-icon">
                    <g fill-rule="evenodd">
                         <path
                         d="M9.667 2.865c-.467-.987-.928-1.582-1.73-1.81C6.9.757 5.66 1.321 5.3 2.343c-.142.404-.212.77-.244 1.064a.83.83 0 01.658.673.824.824 0 01-.661.96.824.824 0 01-.95-.676.83.83 0 01.396-.862c-.056-1.197.681-2.058.681-2.058C6.534-.012 8.152.518 8.645.853c.968.632 1.35 1.412 1.5 1.917a.83.83 0 01.721.683.824.824 0 01-.662.96.824.824 0 01-.95-.676.83.83 0 01.413-.872zm4.9 16.616a2.211 2.211 0 001.728-2.437L14.858 5.769a.276.276 0 01.543-.102l2.995 11.937a2.212 2.212 0 01-1.819 2.72L5.735 21.966a.276.276 0 01-.1-.543l8.933-1.942zM4.4 7.076A2.212 2.212 0 002.572 9.53L3.97 20.642a.276.276 0 01-.543.102L.483 8.968a2.212 2.212 0 011.902-2.73l10.881-1.23a.276.276 0 01.077.546L4.4 7.076z"
                         stroke-width=".5" fill-rule="nonzero"></path>
                         <path
                         d="M5.3 2.344c.36-1.022 1.6-1.586 2.638-1.29.926.265 1.398 1.019 1.95 2.302l.355-.062S10.216 1.88 8.645.853c-.493-.335-2.111-.865-3.466.592 0 0-1.072 1.253-.532 2.835.288.096.397-.139.397-.139s-.105-.775.255-1.797z"
                         stroke-width=".554"></path>
                    </g>
               </symbol>

               <symbol id="vj_study" viewBox="0 0 32 32">
                    <path
                         d="M30.125 17.099v-2.974c0-0.518-0.42-0.938-0.938-0.938-1.937 0-3.742 0.163-5.448 0.497-0.994-0.96-2.207-1.657-3.52-2.038 1.431-1.205 2.343-3.009 2.343-5.022 0-3.653-2.944-6.625-6.563-6.625s-6.563 2.972-6.563 6.625c0 2.013 0.911 3.817 2.343 5.022-1.313 0.381-2.525 1.078-3.52 2.038-1.706-0.334-3.512-0.497-5.448-0.497-0.518 0-0.938 0.42-0.938 0.938v2.974c-1.091 0.387-1.875 1.429-1.875 2.651v1.875c0 1.222 0.784 2.264 1.875 2.651v2.974c0 0.518 0.42 0.938 0.938 0.938 4.902 0 8.927 1.161 12.667 3.655 0.313 0.209 0.726 0.209 1.040 0 3.741-2.494 7.766-3.655 12.667-3.655 0.518 0 0.938-0.42 0.938-0.938v-2.974c1.091-0.387 1.875-1.429 1.875-2.651v-1.875c-0-1.222-0.784-2.264-1.875-2.651zM11.312 6.625c0-2.619 2.103-4.75 4.688-4.75s4.688 2.131 4.688 4.75c0 2.585-2.103 4.688-4.688 4.688s-4.688-2.103-4.688-4.688zM2.812 22.563c-0.517 0-0.938-0.421-0.938-0.938v-1.875c0-0.517 0.421-0.938 0.938-0.938s0.938 0.421 0.938 0.938v1.875c0 0.517-0.421 0.938-0.938 0.938zM15.062 29.381c-3.403-1.946-7.055-2.93-11.312-3.054v-2.050c1.091-0.387 1.875-1.429 1.875-2.651v-1.875c0-1.222-0.784-2.264-1.875-2.651v-2.023c4.405 0.126 7.946 1.164 11.312 3.307v10.997zM16 16.759c-1.73-1.092-3.531-1.923-5.454-2.507 1.056-0.687 2.3-1.064 3.579-1.064h3.75c1.279 0 2.523 0.377 3.579 1.064-1.923 0.584-3.724 1.415-5.454 2.507zM28.25 26.326c-4.257 0.124-7.909 1.108-11.312 3.054v-10.997c3.367-2.144 6.907-3.182 11.312-3.308v2.023c-1.091 0.387-1.875 1.429-1.875 2.651v1.875c0 1.222 0.784 2.264 1.875 2.651v2.050zM30.125 21.625c0 0.517-0.421 0.938-0.938 0.938s-0.938-0.421-0.938-0.938v-1.875c0-0.517 0.421-0.938 0.938-0.938s0.938 0.421 0.938 0.938v1.875z">
                    </path>
               </symbol>
          </defs>
     </svg>    
     <div id="___ndtvpushdiv"></div>
     <!-- jquery min js file here -->

     <script  src="https://www.ndtv.com/dstatic/js/script.js?20220815-4"></script>
     <script  src="https://www.ndtv.com/dstatic/js/fcm-app-message.js?20220815-4"></script>
     <script  src="https://www.ndtv.com/dstatic/js/fcm-config.js?20220815-4"></script>
     <script  src="https://www.ndtv.com/dstatic/js/notification.js?20220815-4"></script>
     
          

          <!-- BROWSER PUSH -->
                         </body>
</html>
'''

soup = BeautifulSoup(html_document , 'html.parser')
soup.prettify()

table = soup.find_all('table',{'class':'font-16 color-blue short-nm'})
# print(table)

tr = table[0].find_all('tr')
print(tr[1])

count = 1
td = 0
while count < len(tr):
     td = tr[count].find_all('td')
     print(td[0].text +  " - " + td[1].text)
     count+=1
# td = tr[2].find_all('td')
# print(td[0].text +  " - " + td[1].text)
# td = tr[3].find_all('td')
# print(td[0].text +  " - " + td[1].text)