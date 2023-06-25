import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class ViabilidadeParceiroService {

constructor(private http: HttpClient) { }

getViabilidadeParceiro() {
  return this.http.get('http://localhost:8000/viabilidade/parceiro/');
}
}
