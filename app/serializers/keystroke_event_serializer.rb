class KeystrokeEventSerializer < ActiveModel::Serializer
  attributes :id, :keystroke, :created_at
  has_one :session
  has_one :keystroke_type
end
