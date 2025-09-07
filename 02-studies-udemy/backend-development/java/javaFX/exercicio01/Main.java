package exercicio01;

import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.layout.BorderPane;
import javafx.scene.control.Button;

public class Main extends Application {
    @Override
    public void start(Stage primaryStage) {
        try {
            BorderPane root = new BorderPane();

            // Adiciona um botão
            Button btn = new Button("Hello World");
            root.setCenter(btn);

            Scene scene = new Scene(root, 400, 400);

            primaryStage.setTitle("Teste JavaFX");
            primaryStage.setScene(scene);
            primaryStage.show();
        } catch(Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        launch(args);
    }
}
