<p>The table of flat.csv</p>
<table> 
<tr>
%for col in rows[0]:
	<th>{{col}}</th>
%end
</tr>

%for row in rows[1:]:
	<tr>
	%for col in row:
		<td>{{col}}</td>
	%end
	</tr>
%end
</table>

