import { Component } from '@angular/core';
import { CdkDragDrop, DragDropModule, moveItemInArray,CdkDragEnd } from '@angular/cdk/drag-drop';
import { CommonModule } from '@angular/common';
import { ProcessNode } from './process-node.model';

@Component({
  selector: 'app-process-block',
  standalone: true,
  imports:[CommonModule, DragDropModule],
  templateUrl: './process-block.component.html',
  styleUrl: './process-block.component.scss',
})
export class ProcessComponent {
  processes: any[] = [];
  selectedType: string | null = null;

  selectBlockType(type: string) {
    this.selectedType = type;

    console.log('==> click : '+this.selectedType);
  }

  placeBlock(event: MouseEvent) {
    console.log("===> placeBlock");

    if (!this.selectedType) return;

    const canvas = (event.currentTarget as HTMLElement).getBoundingClientRect();
    const x = event.clientX - canvas.left;
    const y = event.clientY - canvas.top;

    const newBlock = {
      id: Date.now(),
      name: this.selectedType,
      x,
      y
    };

    this.processes.push(newBlock);
    this.selectedType = null; // 선택 초기화
    this.saveLayout();
  }

  onDragEnd(event: CdkDragEnd, process: any) {
    const pos = event.source.getFreeDragPosition();
    process.x = pos.x;
    process.y = pos.y;
    this.saveLayout();


    console.log("click onDragEnd");
  }

  saveLayout() {
    localStorage.setItem('processLayout', JSON.stringify(this.processes));
  }

  loadLayout() {
    const saved = localStorage.getItem('processLayout');
    if (saved) {
      this.processes = JSON.parse(saved);
    }
  }

  ngOnInit() {
    this.loadLayout();
  }
}