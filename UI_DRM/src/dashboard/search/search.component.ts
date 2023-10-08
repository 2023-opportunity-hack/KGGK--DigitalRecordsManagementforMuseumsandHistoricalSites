import { Component } from '@angular/core';

@Component({
  selector: 'drm-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss']
})
export class SearchComponent {
  value:string ='';

  lengths = Array.from(Array(50).keys()).map(x => x + 1);
} 
