class KeystrokeEvent < ApplicationRecord
  belongs_to :session
  belongs_to :keystroke_type
end
