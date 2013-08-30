var mydata = [
    {"snippetid": 1, "user_answer": "words words words", "score": 0.4, "decoded": "words words words"},
    {"snippetid": 2, "user_answer": "words words words", "score": 0.5, "decoded": "words words words"},
    {"snippetid": 3, "user_answer": "words words words", "score": 0.8, "decoded": "words words words"},
    {"snippetid": 4, "user_answer": "words words words", "score": 0.56, "decoded": "words words words"},
    {"snippetid": 5, "user_answer": "words words words", "score": 0.66, "decoded": "words words words"},
    {"snippetid": 6, "user_answer": "words words words", "score": 1, "decoded": "words words words"},
    {"snippetid": 7, "user_answer": "words words words", "score": 0.8, "decoded": "words words words"},
    {"snippetid": 8, "user_answer": "words words words", "score": 0.06, "decoded": "words words words"},
    {"snippetid": 9, "user_answer": "words words words", "score": 0.9, "decoded": "words words words"},
    {"snippetid": 10, "user_answer": "words words words", "score": 0.7, "decoded": "words words words"},
    {"snippetid": 11, "user_answer": "words words words", "score": 1, "decoded": "words words words"},
    {"snippetid": 12, "user_answer": "words words words", "score": 0.48, "decoded": "words words words"},
    {"snippetid": 13, "user_answer": "words words words", "score": 0.23, "decoded": "words words words"},
    {"snippetid": 14, "user_answer": "words words words", "score": 1, "decoded": "words words words"},
    {"snippetid": 22, "user_answer": "words words words", "score": 0.3, "decoded": "words words words"}
];



var margin = {top: 20, right: 20, bottom: 30, left: 50},
			width = 600 - margin.left - margin.right, //960, 560
			height = 260 - margin.top - margin.bottom; //500, 300

d3.json(mydata, function(lineGraphData) { //where it says "lineGraphData.json" you put "YOURFILE.json"
	var data = lineGraphData;

	var x = d3.scale.linear()
				.domain(d3.extent(data, function(d) { return d.snippetid; }))
	        	.range([0, width]);

	var y = d3.scale.linear()
				.domain([d3.min(data, function(d) { return d.score; }), 1])
				.range([height, 0]);

	var xAxis = d3.svg.axis()
	    		.scale(x)
	    		.tickSubdivide(1)
	    		.orient("bottom");

	var yAxis = d3.svg.axis()
	    		.scale(y)
	    		.orient("left");

	var line = d3.svg.area()
				.x(function(d) { return x(d.snippetid); })
				.y0(height)
				.y1(function(d) { 
					if(d.score > .97)
						{ return y(d.score-.03); }
					else	
						{ return y(d.score); }
				})
				.interpolate("cardinal"); //cardinal

	var line2 = d3.svg.line()
				.x(function(d) { return x(d.snippetid); })
				.y(function(d) { 
					if(d.score > .97)
						{ return y(d.score-.03); }
					else	
						{ return y(d.score); }
				})
				.interpolate("cardinal"); //cardinal

	var lineJayZ = d3.svg.line()
				.x(function(d) { return x(d.snippetid); })
				.y(1)
				.interpolate("basis");

	var svg = d3.select("body").append("svg")
			    .attr("width", width + margin.left + margin.right)
			    .attr("height", height + margin.top + margin.bottom)
			  .append("g")
			    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

	svg.append("g")
			.attr("class", "x axis")
			.attr("transform", "translate(0," + height + ")")
			.call(xAxis);

	svg.append("g")
	      .attr("class", "y axis")
	      .call(yAxis)
	    .append("text")
	      .attr("transform", "rotate(-90)")
	      .attr("y", 6)
	      .attr("dy", ".71em")
	      .style("text-anchor", "end")
	      .text("Score vs Jay-Z   .");

	// svg.append("path")
	//    			.datum(data)
	//    			.attr("class", "line")
	//    			.attr("d", line)
	//    			.style("fill", "url(#gradient)");

	svg.append("path")
			.datum(data)
			.attr("class", "line2")
			.attr("d", line2)
			.style("stroke", "url(#gradient)");

	var gradient = svg
	    .append("svg:linearGradient")
	    .attr("x1", "0%")
	    .attr("y1", "0%")
	    .attr("x2", "0%")
	    .attr("y2", "100%")
	    .attr("id", "gradient")
	    .attr("gradientUnits", "userSpaceOnUse");
	    
	gradient
	    .append("svg:stop")
	    .attr("offset", "0")
	    .attr("stop-color", "#009900"); //f00
	    
	gradient
	    .append("svg:stop")
	    .attr("offset", "0.9")
	    .attr("stop-color", "#fff"); //ff0

	svg.append("path")
		.datum(data)
		.attr("class", "lineJayZ")
		.attr("d", lineJayZ);

		// svg.append("svg:circle")
		// 	.datum(data)
		// 	.attr("class", "point")
		// 	.attr("d", circle);

	svg.selectAll(".dot")
		.data(data)
		.enter().append("circle")
		.attr("class", "dot")
		.attr("r", 3)
		.attr("cx", function(d) { return x(d.snippetid); })
		.attr("cy", function(d) { 
			if(d.score > .97)
				{ return y(d.score-.03); }
			else
				{ return y(d.score); }
		})
		.style("fill", "url(#gradient)")
		//.style("opacity", function(d) { return 1-(1-d.score); })
		.on("mouseover", function(d){
	    	d3.select(this).attr('r', 7);
	    					//.style("stroke", "#000");
	    })
	    .on("mouseout", function(d){
	    	d3.select(this).attr('r', 3);
	    					//.style("stroke", "#009900");
	    })
	    .append("title")
			.text(function(d) { 
			return "Song Snippet ID: " + d.snippetid + "\n" + "Score: " + d.score + "\n" + "Your thoughts: " + d.user_answer;
	    });

	 // ((d.snippetid % d3.min(data, function(d) { return d.snippetid; }))+1)

	svg.selectAll(".dotJayZ")
		.data(data)
		.enter().append("circle")
		.attr("class", "dotJayZ")
		.attr("r", 3)
		.attr("cx", function(d) { return x(d.snippetid); })
		.attr("cy", 1)
		.style("fill", "#FF0000")
		.on("mouseover", function(d){
	    	d3.select(this).attr('r', 7);
	    					//.style("stroke", "#000");
	    })
	    .on("mouseout", function(d){
	    	d3.select(this).attr('r', 3);
	    					//.style("stroke", "#FF0000");
	    })
	    .append("title")
			.text(function(d) { 
			return "Song Snippet ID: " + d.snippetid + "\n" + "Jay-Z's thoughts: " + d.decoded;
	    });
});