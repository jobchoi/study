import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
// import { NxWelcomeComponent } from './nx-welcome.component';

@Component({
  standalone: true,
  imports: [ RouterModule],
  selector: 'app-block-component',
  templateUrl: './block.component.html',
  styleUrl: './block.component.scss',  
})
export class BlockComponent {
  title = 'org.web.leanspire';
}
