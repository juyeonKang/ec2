<p>The table of flat.csv</p>
<table border = "0">
%for row in rows:
	<tr>
	%for col in row:
		<td>{{col}}</td>
	%end
	</tr>
%end
</table>
