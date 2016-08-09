class CreateMouseScrollEvents < ActiveRecord::Migration[5.0]
  def change
    create_table :mouse_scroll_events do |t|
      t.references :session, foreign_key: true
      t.integer :viewport_x
      t.integer :viewport_y

      t.timestamps
    end
  end
end
