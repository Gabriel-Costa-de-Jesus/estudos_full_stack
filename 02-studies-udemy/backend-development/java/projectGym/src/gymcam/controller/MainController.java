package gymcam.controller;

import javafx.fxml.FXML;
import javafx.scene.canvas.Canvas;

public class MainController {

    @FXML private Canvas camera1;
    @FXML private Canvas camera2;
    @FXML private Canvas camera3;
    @FXML private Canvas camera4;
    @FXML private Canvas camera5;
    @FXML private Canvas camera6;

    @FXML
    private void initialize() {
        System.out.println("Inicializando todas as câmeras...");
        // aqui chamamos o service que abre as streams RTSP e joga no Canvas correspondente
    }

    @FXML
    private void focusCamera1() {
        System.out.println("Focar câmera externa 1");
        // lógica para maximizar camera1 na tela
    }

    @FXML
    private void focusCamera2() {
        System.out.println("Focar câmera externa 2");
    }

    @FXML
    private void focusCamera3() {
        System.out.println("Focar câmera Interna 1");
    }

    @FXML
    private void focusCamera4() {
        System.out.println("Focar câmera Interna 2");
    }

    @FXML
    private void focusCamera5() {
        System.out.println("Focar câmera Interna 3");
    }

    @FXML
    private void focusCamera6() {
        System.out.println("Focar câmera Interna 4");
    }
    // ... repete para as outras
}
