class CreateMousePositionEvents < ActiveRecord::Migration[5.0]
  def change
    create_table :mouse_position_events do |t|
      t.references :session, foreign_key: true
      t.integer :position_x
      t.integer :position_y
      t.integer :viewport_x
      t.integer :viewport_y

      t.timestamps
    end
  end
end
