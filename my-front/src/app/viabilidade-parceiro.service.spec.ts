/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { ViabilidadeParceiroService } from './viabilidade-parceiro.service';

describe('Service: ViabilidadeParceiro', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ViabilidadeParceiroService]
    });
  });

  it('should ...', inject([ViabilidadeParceiroService], (service: ViabilidadeParceiroService) => {
    expect(service).toBeTruthy();
  }));
});
