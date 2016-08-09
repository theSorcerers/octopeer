class CreateKeystrokeEvents < ActiveRecord::Migration[5.0]
  def change
    create_table :keystroke_events do |t|
      t.references :session, foreign_key: true
      t.string :keystroke
      t.references :keystroke_type, foreign_key: true

      t.timestamps
    end
  end
end
