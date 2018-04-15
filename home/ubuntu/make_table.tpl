<p>The table of flat.csv</p>
<table cellpadding="5">
<tr>
%for col in rows[0]:
	<th>{{col}}</th>
%end
</tr>
%num=0
%for row in rows[1:]:
	%if num%2==0:
		<tr bgcolor="LightGray">
		%for col in row:
			<td>{{col}}</td>
		%end
		</tr>
	%else:
		<tr>
		%for col in row:
			<td>{{col}}</td>
		%end
		</tr>
	%end
	%num += 1
%end
</table>

