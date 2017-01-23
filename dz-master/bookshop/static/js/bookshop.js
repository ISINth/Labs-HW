function replace(string, string2, container){
	var pos = 0;
	while (true) {
  		var foundPos = document.body.innerHTML.indexOf(string, pos);
  		if (foundPos == -1) break;
  		document.getElementById(container).innerHTML= document.getElementById(container).innerHTML.replace(string, string2);
  		pos = foundPos + 1; // продолжить поиск со следующей
	}
}