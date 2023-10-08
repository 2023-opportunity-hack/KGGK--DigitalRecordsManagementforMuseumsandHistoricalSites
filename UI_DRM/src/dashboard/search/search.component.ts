import { Component } from '@angular/core';
import { DashaboarService, IItems } from '../Service/dashboard.service';
import { HttpParams } from '@angular/common/http';

@Component({
  selector: 'drm-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss']
})
export class SearchComponent {
  value:string ='';

  lengths = Array.from(Array(50).keys()).map(x => x + 1);

  data: IItems[];
  constructor(private _httpService : DashaboarService){


  }


  onSearch(){
    let Params  = {};
    Params['searchText'] = this.value;
    Params['sortBy'] = "Date";

    console.log("ankur")
    this._httpService.getRecords(Params).subscribe((data)=>{

      this.data = data.metaData.Items;

    });
  }
} 
