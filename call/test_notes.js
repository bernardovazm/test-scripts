

// QOL MEET SCREEN SHARE 
var videoShare = document.getElementsByClassName('Gv1mTb-aTv5jf');
var subtitlesContainer = document.getElementsByClassName('a4cQT');

subtitlesContainer[subtitlesContainer.length - 1].style.height = '120px';

if(videoShare[videoShare.length - 1].style.display !== 'none'){
  var divContent = document.getElementsByClassName('xsj2Ff Zf0RDc');
  divContent[divContent.length - 1].style.height = '420px';

  var divContent = document.getElementsByClassName('p2hjYe TPpRNe');
  divContent[divContent.length - 1].style.height = '420px';
};
//

setTimeout(() => {

  // LINK 1: FORD - LIVING BREATHING - SUBTITLES 
  window.open('https://www.youtube.com/embed/NdZZGzR9PxA?autoplay=1','targetWindow',
  `toolbar=no,
   location=no,
   status=no,
   menubar=no,
   scrollbars=yes,
   resizable=yes,
   width=500,
   height=300`).focus();

   /* LINK 2: KID FRANCESCOLI - MOON - CHAT/SECONDARY /
   window.open('https://www.youtube.com/embed/fdixQDPA2h0?autoplay=1','targetWindow',
   `toolbar=no,
    location=no,
    status=no,
    menubar=no,
    scrollbars=yes,
    resizable=yes,
    width=500,
    height=300`).focus();
    */

}, 5000);

/* OLD - Backup


// VERIFICATION OF WORDS

(function(doc,found) {
  console.clear();
  var time = new Date().toLocaleTimeString();
  console.log("Atenção: Habilite a legenda e mantenha o chat aberto. Quanto menor o número de 'mutações', mais próximo estará de mostrar um novo alerta. Um grande número de mutações são realizadas ao interagir na página (Ex: abrir mensagens, lista de pessoas, habilitar legenda etc). Você já pode fechar esse console agora. ");
  
  // Número de mutações
  let mutationLimit = 150;

  let countOverall = 0;
  let countChat = 10;
  let countSub = 0;

  var observer = new MutationObserver(function(mutations) {
      mutations.forEach(function(mutation) {
        countOverall += 1;

        var sub = document.getElementsByClassName('CNusmb');
        for (var i = 0, len = sub.length; i < len; ++i) {
          if(sub[i].innerHTML.indexOf("presente") !== -1 || sub[i].innerHTML.indexOf("chamada") !== -1 || sub[i].innerHTML.indexOf("presença") !== -1 || sub[i].innerHTML.indexOf("Bernardo") !== -1 || sub[i].innerHTML.indexOf("Alexandre") !== -1) {
            
            // - Execução de alerta caso palavra exista na legenda
            countSub += 1;

            if(countSub === 1 && found === false) {
              countSub = 0;
              found = true;
              console.log("[SUB] - Found: '" + sub[i].innerHTML + "' at " + time + ".");
              window.open('https://www.youtube.com/watch?v=NdZZGzR9PxA', '_blank').focus();
              // window.alert("asd");
              console.log("New alerts will be ignored for the next " + (mutationLimit - countOverall) + " mutations.");
            };

          };
        };

        var chat = document.getElementsByClassName('oIy2qc');
        for (var ic = 0, lenc = chat.length; ic < lenc; ++ic) {
          //console.log(chat[ic].innerHTML, countOverall);
          if(chat[ic].innerHTML.indexOf("presente") !== -1 || chat[ic].innerHTML.indexOf("chamada") !== -1 || chat[ic].innerHTML.indexOf("presença") !== -1 || chat[ic].innerHTML.indexOf("Bernardo") !== -1 || chat[ic].innerHTML.indexOf("P") !== -1 ||chat[ic].innerHTML.indexOf("p") !== -1) {
            
            // - Execução de alerta caso palavra exista no chat
            countChat += 1;

            if(countChat === 1 && found === false) {
              found = true;
              console.log("[CHAT] - Found: '" + chat[ic].innerHTML + "' at " + time + ".");
              window.open('https://www.youtube.com/watch?v=Ivrrt6oYxxc').focus();
              // window.alert("[CHAT] - Found: '" + chat[ic].innerHTML + "' at " + time + ".");
              console.log("New alerts will be ignored for the next " + (mutationLimit - countOverall) + " mutations.");
            };

          };
        };

        if(countOverall >= mutationLimit){
          console.log("Alerts recycled. New tab will open if a word is found.");

          //countChat = 0;
          countOverall = 0;
          countSub = 0;
          found = false;
        };

      });
  });
  observer.observe(doc, { childList: true, subtree: true });
})(document,false);

//

WIP*/



// MEET QOL & AUTOMATIC PRESENCE ANSWERER SCRIPT

setTimeout(() => {
(function(doc) {
  console.clear();
  function currentTime() {
    fullDate = new Date();
    dateString = fullDate.toLocaleTimeString();
    return dateString;
  };
  console.log("[INFO] - WIP - Script started at " + currentTime() + ". If you send any message in chat, the automatic message will not be sent. ");

  const subWords1 = ["Presença", "Presente", "Chamada", "presença", "presente", "chamada"];
  var isSubWord1Found = false;

  const subWords2 = ["Alan", "André", "Alexandre"];
  var isSubWord2Found = false;

  const subWords3 = ["Bernardo", "Bernardo Vaz", "Bernardo Melo", "Bernardo Oliveira", "Bernardo Vaz de Melo Oliveira"];
  var isSubWord3Found = false;

  const chatWords = ["Presente", "presente", "P", "p"];
  var isChatWordFound = false;

  var timeoutDelay = 300000;

  // SETTING MEET READY / SHUTTING DOWN EVERYTHING - "join" screen

  // step 1.1: cam blocked popup
  var camPopup = document.getElementsByClassName('Ce1Y1c')[0];

  if(!!camPopup){
    camPopup.click();
  };

  // step 1.2: cam/mic blocked popup
  var miccamPopup = document.getElementsByClassName('RveJvd snByac')[5];
  
  if(!!miccamPopup){
    miccamPopup.click();
  };

  // step 2: close mic/cam
  var micCamButtons = document.getElementsByClassName('U26fgb JRY2Pb mUbCce kpROve yBiuPb y1zVCf HNeRed M9Bg4d');

  if(micCamButtons.length !== 0){
    for (var micCamCounter = 0, micCamLenght = micCamButtons.length; micCamCounter < micCamLenght; ++micCamCounter) {
      micCamButtons[0].click();
    };
  };

  // JOINING ROOM - "join" screen
  /*
  // step 1: verif acc and fixing link to log into the right account
  var account = "72000724@aluno.faculdadecotemig.br";
  var authuser = "?authuser=3";

  var currentAccount = document.getElementsByClassName('ASy21 Duq0Bf')[0];
  var currentLink = window.location.href;

  !!currentAccount && (currentAccount.textContent !== account && window.location.replace(currentLink+authuser));
  // currentLink.indexOf(authuser) === -1 && window.location.replace(currentLink+authuser);

  // step 2: joining room from "join" screen
  var joinButton = document.getElementsByClassName('uArJ5e UQuaGc Y5sE8d uyXBBb xKiqt')[0];

  !!joinButton && (
    setTimeout(() => {
      joinButton.click();
    }, 500));
  */

  // KEYWORDS IDENTIFIER AND POST
  var observer = new MutationObserver(function(mutations) {
      mutations.forEach(function(mutation) {
        
        // Closing cam/mic popups inside room
        var dismissPopupButton = document.getElementsByClassName('RveJvd snByac')[3];

        if(!!dismissPopupButton) { 
          dismissPopupButton.click()
        };

        // SETTING ROOM - subs
        // step 1: verify if subtitles not on and activating
        var isSubtitlesOff = document.getElementsByClassName('a4cQT')[0];
        var moreOptionsButton = document.getElementsByClassName('VfPpkd-Bz112c-LgbsSe yHy1rc eT1oJ tWDL4c uaILN')[3];
      
        var subtitlesOptionsButton = document.getElementsByClassName('V4jiNc ACt4Tb VfPpkd-StrnGf-rymPhb-ibnC6b')[1];
      
        var portugueseLabel = document.getElementsByClassName('Od2TWd hYsg7c')[5];
      
        var applySubtitlesButton = document.getElementsByClassName('RveJvd snByac')[5];
      
        if(!!isSubtitlesOff && !!isSubtitlesOff.style){
          if(isSubtitlesOff.style.display === "none" && !portugueseLabel && !subtitlesOptionsButton){
            setTimeout(() => {
              moreOptionsButton.click()
            }, 500)
          };
      
          // step 2
          !!subtitlesOptionsButton && (
              subtitlesOptionsButton.click()
          );
        
          // step 3: setting label
          !!portugueseLabel && (
              portugueseLabel.click()
          );
        
          // step 4: apply portuguese subtitle
          !!applySubtitlesButton && (
              applySubtitlesButton.click()
          );      
        };

        // SETTING ROOM - chat
        // step 1: verify if chat not on and activating
        var chatButton = document.getElementsByClassName('VfPpkd-Bz112c-LgbsSe yHy1rc eT1oJ JsuyRc boDUxc')[2];

        if(!!chatButton) {
          var chatButtonAttribute = chatButton.getAttribute('aria-pressed');
          if(chatButtonAttribute === "false"){
            chatButton.click()
          };
        };

        // QOL MEET SCREEN SHARE 
        //var videoShare = document.getElementsByClassName('Gv1mTb-aTv5jf');
        var subtitlesContainer = document.getElementsByClassName('a4cQT');

        subtitlesContainer[subtitlesContainer.length - 1].style.height = '120px';

        //if(videoShare[videoShare.length - 1].style.display !== 'none'){
          //var divContent1 = document.getElementsByClassName('xsj2Ff Zf0RDc');
          // divContent1[divContent1.length - 1].style.height = '420px';
          // //divContent1[divContent1.length - 1].style.width = '600px';

          // var divContent2 = document.getElementsByClassName('p2hjYe TPpRNe');
          // divContent2[divContent2.length - 1].style.height = '420px';
          // divContent2[divContent2.length - 1].style.width = '600px';
        //};
        //

        // CHAT AND SUBTITLES IDENTIFIER
        var chatArray = document.getElementsByClassName('oIy2qc');

        var subArray = document.getElementsByClassName('CNusmb');

        // CHECKERS
        for (var subCount = 0, subLenght = subArray.length; subCount < subLenght; ++subCount) {
          if(!isSubWord1Found && !isSubWord3Found){
            for (var wordsCount = 0, wordsLenght = subWords1.length; wordsCount < wordsLenght; ++wordsCount) {            
              if(subArray[subCount].innerHTML.indexOf(subWords1[wordsCount]) !== -1){
                  isSubWord1Found = true;
                  window.open('https://www.youtube.com/embed/NdZZGzR9PxA?autoplay=1','targetWindow',`toolbar=no,location=no,status=no,menubar=no,scrollbars=yes,resizable=yes,width=500,height=300`).focus();
                  
                  console.log("[SUB 1] - Found: word '" + subWords1[wordsCount] + "' in '" + subArray[subCount].innerHTML + "' at " + currentTime() + ".");
                  
                  var notification = new Notification('Lista de palavras 1 identificado na legenda', {
                    body: 'Chamada pode começar',
                  });
                  notification.onclick = function() {
                    window.focus();
                  };
                
                setTimeout(() => {
                  isSubWord1Found = false;
                  console.log("[SUB 1] - Previous warning ignored.");
                }, timeoutDelay);
              }
            };
          };

            if(!isSubWord2Found && isSubWord1Found && !isSubWord3Found){              
              for (var wordsCount = 0, wordsLenght = subWords2.length; wordsCount < wordsLenght; ++wordsCount) {            
                if(subArray[subCount].innerHTML.indexOf(subWords2[wordsCount]) !== -1){
                  isSubWord2Found = true;
                  
                  console.log("[SUB 2] - Found: word '" + subWords2[wordsCount] + "' in '" + subArray[subCount].innerHTML + "' at " + currentTime() + ".");
                
                  setTimeout(() => {
                    isSubWord2Found = false;
                    console.log("[SUB 2] - Previous warning ignored.");
                  }, timeoutDelay);   
                }
              };
            };

            // CHECKER 3 & POST
            if(!isSubWord3Found && (isSubWord1Found && isSubWord2Found || isChatWordFound)){
              for (var wordsCount = 0, wordsLenght = subWords3.length; wordsCount < wordsLenght; ++wordsCount) {            
                if(subArray[subCount].innerHTML.indexOf(subWords3[wordsCount]) !== -1){
                  isSubWord3Found = true;
                  
                  // SETTING 'PRESENTE' IN TEXTFIELD
                  // Hard verificate before setting message
                  var messageSent = false;
                  var myChatTitleFound = false;

                  var chatLabel = document.getElementsByClassName('KHxj8b tL9Q4c')[0];
                  var sendButton = document.getElementsByClassName('VfPpkd-Bz112c-LgbsSe yHy1rc eT1oJ tWDL4c Cs0vCd')[0];
                  var chatTitleList = document.getElementsByClassName('YTbUzc');

                  // Verification if any message was already sent
                  if(chatTitleList.length !== 0){
                    for (
                      var chatTitleListCounter = 0, chatTitleListLenght = chatTitleList.length;
                      chatTitleListCounter < chatTitleListLenght;
                      ++chatTitleListCounter
                      ) 
                    {
                      if(chatTitleList[chatTitleListCounter].textContent === 'Você'){
                        myChatTitleFound = true;   
                      };
                    };
                  } else{
                    console.log("[SUB 3] - Alert - Automatic message could not be sent because 'You' was identified previously in chat. - " + currentTime());
                  };
                  
                  console.log("[SUB 3] - Sent - Found: word '" + subWords3[wordsCount] + "' in '" + subArray[subCount].innerHTML + "' at " + currentTime() + ".");

                  if (!messageSent && !myChatTitleFound && !!chatLabel && !!sendButton) {
                    setTimeout(() => {
                      chatLabel.value = "Presente";
                      sendButton.removeAttribute("disabled");
                      sendButton.click();
                      messageSent = true;
                    }, 292);
                  };
                    
                    var notification = new Notification('Nome identificado durante chamada - Presente enviado automaticamente no chat', {
                      body: 'Chamada finalizada.',
                    });
                    notification.onclick = function() {
                      window.focus();
                    };
                }
              };
            };


        };

        // CHECKER - CHAT
        for (var chatCount = 0, chatLenght = chatArray.length; chatCount < chatLenght; ++chatCount) {
          if(!isChatWordFound && !isSubWord3Found){
            for (var wordsCount = 0, wordsLenght = chatWords.length; wordsCount < wordsLenght; ++wordsCount) {            
              if(chatArray[chatCount].innerHTML === chatWords[wordsCount]){
                  isChatWordFound = true;
                  window.open('https://www.youtube.com/embed/fdixQDPA2h0?autoplay=1','targetWindow',`toolbar=no,location=no,status=no,menubar=no,scrollbars=yes,resizable=yes,width=500,height=300`).focus();    
                  
                  console.log("[CHAT] - Found: word '" + chatWords[wordsCount] + "' in '" + chatArray[chatCount].innerHTML + "' at " + currentTime() + ".");
                  
                  var notification = new Notification('Alguém está respondendo presença no chat', {
                    body: 'Chamada pode ter começado',
                  });
                  notification.onclick = function() {
                    window.focus();
                  };
                  
                  setTimeout(() => {
                    isChatWordFound = false;
                    console.log("[CHAT] - Previous warning ignored.");
                  }, timeoutDelay); 

              }
            };
          };
        };
      });
  });
  observer.observe(doc, { childList: true, subtree: true });
})(document,false);
}, 5000);

// 







// SETTING 'PRESENTE' IN TEXTFIELD
// Hard verificate before setting message
var messageSent = false;
var myChatTitleFound = false;

var chatLabel = document.getElementsByClassName('KHxj8b tL9Q4c')[0];
var sendButton = document.getElementsByClassName('VfPpkd-Bz112c-LgbsSe yHy1rc eT1oJ tWDL4c Cs0vCd')[0];
var chatTitleList = document.getElementsByClassName('YTbUzc');

// Verification if message already sent
if(chatTitleList.length !== 0){
  for (
    var chatTitleListCounter = 0, chatTitleListLenght = chatTitleList.length;
    chatTitleListCounter < chatTitleListLenght;
    ++chatTitleListCounter
    ) 
  {
    if(chatTitleList[chatTitleListCounter].textContent === 'Você'){
      myChatTitleFound = true;   
    };
  };
};

if (!messageSent && !myChatTitleFound && !!chatLabel && !!sendButton) {
  setTimeout(() => {
    chatLabel.value = "Presente";
    sendButton.removeAttribute("disabled");
    sendButton.click(), messageSent = true;
  }, 292);
};









// SETTING MEET READY / SHUTTING DOWN EVERYTHING - "join" screen

// step 1.1: cam blocked popup
var camPopup = document.getElementsByClassName('Ce1Y1c')[0];

if(!!camPopup){
  camPopup.click();
};

// step 1.2: cam/mic blocked popup
var miccamPopup = document.getElementsByClassName('RveJvd snByac')[5];

if(!!miccamPopup){
  miccamPopup.click();
};


// step 2: close mic/cam
var micCamButtons = document.getElementsByClassName('U26fgb JRY2Pb mUbCce kpROve yBiuPb y1zVCf HNeRed M9Bg4d');

if(micCamButtons.length !== 0){
  for (var micCamCounter = 0, micCamLenght = micCamButtons.length; micCamCounter < micCamLenght; ++micCamCounter) {
    micCamButtons[0].click();
  };
};


// JOINING ROOM - "join" screen

// step 1: verif acc and fixing link to log into the right account
var account = "bernardovazmelo@gmail.com";
var authuser = "?authuser=3";

var currentAccount = document.getElementsByClassName('ASy21 Duq0Bf')[0];
var currentLink = window.location.href;

!!currentAccount && (currentAccount.textContent !== account && window.location.replace(currentLink+authuser));
// currentLink.indexOf(authuser) === -1 && window.location.replace(currentLink+authuser);


// step 2: joining room from "join" screen
var joinButton = document.getElementsByClassName('uArJ5e UQuaGc Y5sE8d uyXBBb xKiqt')[0];

!!joinButton && (
setTimeout(() => {
  joinButton.click()
}, 500)
);


// Closing cam/mic popups inside room
var dismissPopupButton = document.getElementsByClassName('RveJvd snByac')[3];

!!dismissPopupButton && dismissPopupButton.click();


// SETTING ROOM - subs
  // step 1: verify if subtitles not on and activating
    var isSubtitlesOff = document.getElementsByClassName('a4cQT')[0];
    var moreOptionsButton = document.getElementsByClassName('VfPpkd-Bz112c-LgbsSe yHy1rc eT1oJ tWDL4c uaILN')[3];
  
    var subtitlesOptionsButton = document.getElementsByClassName('V4jiNc ACt4Tb VfPpkd-StrnGf-rymPhb-ibnC6b')[1];
  
    var portugueseLabel = document.getElementsByClassName('Od2TWd hYsg7c')[5];
  
    var applySubtitlesButton = document.getElementsByClassName('RveJvd snByac')[5];
  
    if(!!isSubtitlesOff && !!isSubtitlesOff.style){
      if(isSubtitlesOff.style.display === "none" && !portugueseLabel && !subtitlesOptionsButton){
        setTimeout(() => {
          moreOptionsButton.click()
        }, 500)
      };
  
      // step 2
      !!subtitlesOptionsButton && (
          subtitlesOptionsButton.click()
      );
    
      // step 3: setting label
      !!portugueseLabel && (
          portugueseLabel.click()
      );
    
      // step 4: apply portuguese subtitle
      !!applySubtitlesButton && (
          applySubtitlesButton.click()
      );
  
    };

// SETTING ROOM - chat
// step 1: verify if chat not on and activating
var chatButton = document.getElementsByClassName('VfPpkd-Bz112c-LgbsSe yHy1rc eT1oJ JsuyRc boDUxc')[2];

!!chatButton && (chatButton.getAttribute('aria-pressed') === 'false' && chatButton.click());




















// VERIFICATION OF WORDS 2.0

setTimeout(() => {

  (function(doc,found) {
    console.clear();
    var time = new Date().toLocaleTimeString();
    console.log("Atenção: Habilite a legenda e mantenha o chat aberto. Quanto menor o número de 'mutações', mais próximo estará de mostrar um novo alerta. Um grande número de mutações são realizadas ao interagir na página (Ex: abrir mensagens, lista de pessoas, habilitar legenda etc). Você já pode fechar esse console agora. ");
    
    // Número de mutações
    let mutationLimit = 150;
    const keywords = ["banana", "mango"];
  
    let countMutations = 0;
    let countChat = 0;
    let countSub = 0;
  
    
    // SETTING MEET READY / SHUTTING DOWN EVERYTHING - "join" screen
  
    // step 1.1: cam blocked popup
    var camPopup = document.getElementsByClassName('Ce1Y1c')[0];
  
    if(!!camPopup){
      camPopup.click();
    };
  
    // step 1.2: cam/mic blocked popup
    var miccamPopup = document.getElementsByClassName('RveJvd snByac')[5];
    
    if(!!miccamPopup){
      miccamPopup.click();
    };
  
    // step 2: close mic/cam
    var micCamButtons = document.getElementsByClassName('U26fgb JRY2Pb mUbCce kpROve yBiuPb y1zVCf HNeRed M9Bg4d');
  
    if(micCamButtons.length !== 0){
      for (var micCamCounter = 0, micCamLenght = micCamButtons.length; micCamCounter < micCamLenght; ++micCamCounter) {
        micCamButtons[0].click();
      };
    };
  
    // JOINING ROOM - "join" screen
  
    // step 1: verif acc and fixing link to log into the right account
    var account = "72000724@aluno.faculdadecotemig.br";
    var authuser = "?authuser=3";
  
    var currentAccount = document.getElementsByClassName('ASy21 Duq0Bf')[0];
    var currentLink = window.location.href;
  
    !!currentAccount && (currentAccount.textContent !== account && window.location.replace(currentLink+authuser));
    // currentLink.indexOf(authuser) === -1 && window.location.replace(currentLink+authuser);
  
    // step 2: joining room from "join" screen
    var joinButton = document.getElementsByClassName('uArJ5e UQuaGc Y5sE8d uyXBBb xKiqt')[0];
  
    !!joinButton && (
      setTimeout(() => {
        joinButton.click();
      }, 500));
  
    var observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
  
    // Closing cam/mic popups inside room
    var dismissPopupButton = document.getElementsByClassName('RveJvd snByac')[3];
  
    !!dismissPopupButton && dismissPopupButton.click();
            
    // SETTING ROOM - subs
    // step 1: verify if subtitles not on and activating
    var isSubtitlesOff = document.getElementsByClassName('a4cQT')[0];
    var moreOptionsButton = document.getElementsByClassName('VfPpkd-Bz112c-LgbsSe yHy1rc eT1oJ tWDL4c uaILN')[3];
  
    var subtitlesOptionsButton = document.getElementsByClassName('V4jiNc ACt4Tb VfPpkd-StrnGf-rymPhb-ibnC6b')[1];
  
    var portugueseLabel = document.getElementsByClassName('Od2TWd hYsg7c')[5];
  
    var applySubtitlesButton = document.getElementsByClassName('RveJvd snByac')[5];
  
    if(!!isSubtitlesOff && !!isSubtitlesOff.style){
      if(isSubtitlesOff.style.display === "none" && !portugueseLabel && !subtitlesOptionsButton){
        setTimeout(() => {
          moreOptionsButton.click()
        }, 500)
      };
  
      // step 2
      !!subtitlesOptionsButton && (
          subtitlesOptionsButton.click()
      );
    
      // step 3: setting label
      !!portugueseLabel && (
          portugueseLabel.click()
      );
    
      // step 4: apply portuguese subtitle
      !!applySubtitlesButton && (
          applySubtitlesButton.click()
      );
  
    };
  
    //!!isSubtitlesOff && (isSubtitlesOff.style.display === 'none' && !portugueseLabel && moreOptionsButton.click());
  
    // SETTING ROOM - chat
    // step 1: verify if chat not on and activating
    var chatButton = document.getElementsByClassName('VfPpkd-Bz112c-LgbsSe yHy1rc eT1oJ JsuyRc boDUxc')[2];
  
    !!chatButton && (chatButton.getAttribute('aria-pressed') === 'false' && chatButton.click());
  
  
          countMutations += 1;
  
          var chat = document.getElementsByClassName('oIy2qc');
          var volumeElement = document.getElementsByClassName('ScCoreButton-sc-1qn4ixc-0 fVEFfF ScButtonIcon-sc-o7ndmn-0 jGcDiv')[1].ariaLabel;

          for (var ic = 0, lenc = chat.length; ic < lenc; ++ic) {          
            for (var wordsCount = 0, wordsLenght = keywords.length; wordsCount < wordsLenght; ++wordsCount) {            
              console.log("LOG VERIF", chat[ic].innerHTML.indexOf(keywords[wordsCount]) !== -1);  
            };
          };
  
          if(countMutations >= mutationLimit){
            console.log("Alerts recycled. New tab will open if a word is found.");
  
            countMutations = 0;
            countSub = 0;
            found = false;
          };
  
        });
    });
    observer.observe(doc, { childList: true, subtree: true });
  })(document,false);

}, 5000);

//



















