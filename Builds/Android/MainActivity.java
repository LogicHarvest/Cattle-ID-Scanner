import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Button;
import android.widget.Toast;
import io.chaquopy.py.*;

public class MainActivity extends AppCompatActivity {

    static {
        System.loadLibrary("native-lib");
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize Chaquopy
        if (!Python.isStarted()) {
            Python.start(new AndroidPlatform(this));
        }

        // Find the button in the layout
        Button runButton = findViewById(R.id.runButton);

        // Set a click listener for the button
        runButton.setOnClickListener(view -> {
            // Execute the Python script
            try {
                Python.getInstance().getModule("app").callAttr("main");
            } catch (Exception e) {
                e.printStackTrace();
            }

            // Display a toast (optional)
            Toast.makeText(MainActivity.this, "Python script executed!", Toast.LENGTH_SHORT).show();
        });
    }
}
