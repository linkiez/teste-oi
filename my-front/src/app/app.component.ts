import { Component, OnInit } from '@angular/core';
import { ViabilidadeParceiroService } from './viabilidade-parceiro.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {

  viabilidade: any = [];

  constructor(private viabilidadeParceiroService: ViabilidadeParceiroService)
  {}

  ngOnInit(): void {
    this.viabilidadeParceiroService.getViabilidadeParceiro()
      .subscribe(response => {this.viabilidade = response});
  }

}
