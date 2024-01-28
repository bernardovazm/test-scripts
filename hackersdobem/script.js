setTimeout(() => {
(function(doc) {
  console.clear();
  function currentTime() {
    fullDate = new Date();
    dateString = fullDate.toLocaleTimeString();
    return dateString;
  };
  console.log("[INFO] - WIP - Script started at " + currentTime() + ". ");
  var observer = new MutationObserver(function(mutations) {
      mutations.forEach(function(mutation) {
        console.log(`[] new mutation ${mutation}`);

        function clickObj(obj) {
          setTimeout(() => {
            console.log(`[] ${obj} got clicked at ${currentTime()}`);
            obj.click()
          }, 1100);
        }
  
        const buttonContinue = document.getElementsByClassName('continue-btn brand--ui');
        const inputRadio = document.getElementsByClassName('quiz-multiple-choice-option__label brand--body cursorAuto brand--linkColor');
        const buttonAnswer = document.getElementsByClassName('quiz-card__button');
        const inputRadio2 = document.getElementsByClassName('quiz-multiple-choice-option');
        let listCollections = [buttonContinue, inputRadio, buttonAnswer, inputRadio2];

        listCollections.forEach(collection => {
          collection.forEach(object => {
            if(object){
              clickObj(object);
            };
          });
        });

      });
  });
  observer.observe(doc, { childList: true, subtree: true });
})(document,false);
}, 5000);
