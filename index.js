var myvar;
		$('.plot').click(function(e) {
			clearInterval(myvar)
			console.log(myvar)
			var x=parseFloat($('.from').val())
			const x1=x
			const xn=parseFloat($('.to').val())
			const fun=$('.fun').val()
			var points=[x,eval(fun)]
			
			console.log(points)
			console.log(fun);
			myvar=setInterval(function(){
				$.plot($('.graph'), [ { label: fun, data: points } ], {});
				x=x+(xn-x1)/100
				if (points.length > 100){
					points.splice(1,1)
				};
				points.push([x,eval(fun)])
			}, 100);
			console.log(myvar)
		});