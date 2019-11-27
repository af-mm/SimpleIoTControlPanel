function activateAction(globalActionId){
	var e = document.getElementById("a" + globalActionId);
	var delay = 5000;
	
	fetch("/api/activateAction?globalActionId=" + globalActionId)
		.then(function(d){
			return d.json();
		})
		.then(function(d){
			if(d.result == 0){
				e.classList.toggle("failure", 1);
				setTimeout(function(){
					e.classList.toggle("failure", 0);
				}, delay);
				throw new Error("d.result != 1");
			}else{
				e.classList.toggle("success", 1);
				setTimeout(function(){
					e.classList.toggle("success", 0);
				}, delay);
			}
				
		})
		.catch(function(err){
			e.classList.toggle("failure", 1);
			setTimeout(function(){
				e.classList.toggle("failure", 0);
			}, delay);
			console.log(err);
		});
}
