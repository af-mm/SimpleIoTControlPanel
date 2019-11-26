function activateAction(globalActionId){
	fetch("/api/activateAction?globalActionId=" + globalActionId)
		.then(function(d){
			return d.json();
		})
		.then(function(d){
			if(d.result == 0)
				throw new Error("123");
		})
		.catch(function(err){
			console.log(err);
		});
}
