import { Component, OnInit } from '@angular/core';
import { FormArray, FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { MatChipInputEvent } from '@angular/material/chips';
import { AlertData } from 'src/shared/interfaces';
import { ENTER, COMMA } from '@angular/cdk/keycodes';
import { HttpClient } from '@angular/common/http';
import { throwError } from 'rxjs';
import {MatSnackBar} from '@angular/material/snack-bar';


@Component({
  selector: 'drm-add-file',
  templateUrl: './add-file.component.html',
  styleUrls: ['./add-file.component.scss']
})
export class AddFileComponent implements OnInit {
  
  metaDataFileName: string = '';
  file: File = null;
  fileReader: FileReader;
  showAlert:boolean = false;
  separatorKeysCodes: number[] = [ENTER, COMMA];

  uploadForm: FormGroup;

  status: string ='';


  //remove below code

  keywords : any[] = ['ankru','patel']

  alertData: AlertData = {
    alertType: '',
    message: '',
  }


  constructor(private fb: FormBuilder, private _http: HttpClient, private _snackBar: MatSnackBar){}

  ngOnInit(): void {
    this.uploadForm = this.fb.group({
      keywords : this.fb.array([]),
      uploadedAt : [''],
      metadata : ['',Validators.required ]      
      // samlRadio: samlRadioButton.MANUAL,
    });

    this.fileReader = new FileReader();
    this.fileReader.onload = () => {
      if(this.fileReader.result==""){
        // this.alertData.message = "XML File can not be empty";
        // this.showAlert = true;
      }
      else{
        // this.showAlert = false;
      }
      this.uploadForm.patchValue({
        metaData: this.fileReader.result,
      });
      // this.cd.markForCheck();
    }
    
  }



  metadataFile(event, eventType: string) {
    const reader = new FileReader();


    switch (eventType) {
      case "fileDropped":
        this.metaDataFileName = event[0].name;
        this.file = event[0];
        if(this.xmlFileTypeError(event[0])){return;}
        this.fileReader.readAsText(event[0]);
        break;

      case "fileUploaded":
        this.metaDataFileName = event.target.files[0].name;
        this.file = event.target.files[0];
        if(this.xmlFileTypeError(event.target.files[0])){return;}
        this.fileReader.readAsText(event.target.files[0]);
        break;
    }
  }

  xmlFileTypeError(file:File){
    if (this.file) {
      const formData = new FormData();
  
      formData.append('file', this.file, this.file.name);
  
      const upload$ = this._http.post("https://httpbin.org/post", formData);
  
      this.status = 'uploading';
  
      upload$.subscribe({
        next: () => {
          this.status = 'success';
          console.log("success");
        },
        error: (error: any) => {
          this.status = 'fail';
          console.log("fail");
          return throwError(() => error);
        },
      });
    }




    this.showAlert = false;
    if(file.type=='text/xml'){
      return false;
    }else{
      this.uploadForm.patchValue({
        metaData: '',
      });
      this.alertData.message = 'File Type must be XML'
      this.showAlert = true;
      return true;
    }
  }


  addKeyword(event: MatChipInputEvent): void {

    const input = event.input;
    const value = event.value.split(',');
    value.forEach(val=>this.addControl(val.trim(),"keywords"));
    if (input) {
      input.value = "";
    }
  }

  addControl(value,controlName){
    if (value) {
      const keywordArrayControl = this.uploadForm.controls[controlName] as FormArray;
      const keywordControl = this.getControl();
      keywordControl.setValue(value.trim())
      if(keywordControl?.valid && !keywordArrayControl?.value?.includes(value)){
        keywordArrayControl.push(keywordControl);
        this.uploadForm.markAsDirty();
      }
    }

    
  }

  getControl(): FormControl {
    return this.fb.control(['']);
  }

  removeKeyword(index : number): void {

    (this.uploadForm.controls["keywords"] as FormArray).removeAt(index);

  }

  upload(){
    console.log(this.uploadForm.value)

    if(!this.uploadForm.valid) {
      const ref =   this._snackBar.open('Please Upload the file first');
      setTimeout(()=>{
        ref.dismiss();
      },2000);
    }

    
  }

}
